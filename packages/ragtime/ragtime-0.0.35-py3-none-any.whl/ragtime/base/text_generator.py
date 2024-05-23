#!/usr/bin/env python3

from abc import ( abstractmethod, ABC )

from ragtime.base.retriever import ( Retriever )
from ragtime.base.llm import *

from ragtime.expe import ( Expe, RagtimeBase, QA )
from ragtime.config import ( RagtimeException, logger )

from typing import ( Optional )
import asyncio

from ragtime.expe import ( Answer, Answers, QA ) # TODO: This double name can be miss leading

from enum import IntEnum
class StartFrom(IntEnum):
	beginning = 0
	chunks = 1
	prompt = 2
	llm = 3
	post_process = 4


class TextGenerator(RagtimeBase, ABC):
    """
    Abstract class for AnswerGenerator, FactGenerator, EvalGenerator
    """
    llms:Optional[list[LLM]] = []
    b_use_chunks:bool = False

    def __init__(self, llms:list[LLM] = None):
        """
        Args
            llms(LLM or list[LLM]) : list of LLM objects
        """
        super().__init__()
        if (not llms):
            raise RagtimeException('llms lists is empty! Please provide at least one.')
        if isinstance(llms, LLM): llms = [llms]
        self.llms +=  llms


    @property
    def llm(self) -> LLM:
        """
        Helper function to get the first LLM when only one is provided (like for EvalGenerator and FactGenerator)
        """
        if not self.llms:
            return None
        return self.llms[0]


    def generate(
            self,
            expe:Expe,
            save_every:int = 0,
            b_missing_only:bool = False,
            only_llms:list[str] = None,
            start_from:StartFrom = StartFrom.beginning,
    ):
        """
        Main method calling "gen_for_qa" for each QA in an Expe. Returns False if completed with error, True otherwise
        The main step in generation are :
        - beginning: start of the process - when start_from=beginning, the whole process is executed
	    - chunks: only for Answer generation - chunk retrieval, if a Retriever is associated with the Answer Generator object
        Takes a Question and returns the Chunks
        - prompt: prompt generation, either directly using the question or with the chunks if any
        Takes a Question + optional Chunks and return a Prompt
        - llm: calling the LLM(s) with the generated prompts
        Takes a Prompt and return a LLMAnswer
        - post_process: post-processing the aswer returned by the LLM(s)
        Takes LLMAnswer + other information and updates the Answer object
        Args:
            - expe: Expe object to generate for
            - start_from: allows to start generation from a specific step in the process
            - b_missing_only: True to execute the steps only when the value is absent, False to execute everything
            even if a value already exists
            - only_llms: restrict the llms to be computed again - used in conjunction with start_from -
            if start from beginning, chunks or prompts, compute prompts and llm answers for the list only -
            if start from llm, recompute llm answers for these llm only - has not effect if start
            """

        logger.prefix += f"[{self._name}]"
        nb_q:int = len(expe)
        async def _generate_for_qa(num_q:int, qa:QA):
            logger.prefix = f"({num_q}/{nb_q})"
            logger.info(f'*** {self.__class__.__name__} for question \n"{qa.question.text}"')
            try:
                await self.gen_for_qa(
                    qa=qa,
                    start_from=start_from,
                    b_missing_only=b_missing_only,
                    only_llms=only_llms
                )
            except Exception as e:
                logger.exception(f"Exception caught - saving what has been done so far:\n{e}")
                expe.save_to_json()
                expe.save_temp(name=f"Stopped_at_{num_q}_of_{nb_q}_")
                return
            logger.info(f'End question "{qa.question.text}"')
            if save_every and (num_q % save_every == 0): expe.save_to_json()

        loop = asyncio.get_event_loop()
        tasks = [_generate_for_qa(num_q, qa) for num_q, qa in enumerate(expe, start=1)]
        logger.info(f'{len(tasks)} tasks created')
        loop.run_until_complete(asyncio.gather(*tasks))

    def write_chunks(self, qa:QA):
        """Write chunks in the current qa if a Retriever has been given when creating the object. Ignore otherwise"""
        raise NotImplementedError('Must implement this if you want to use it!')


    @abstractmethod
    async def gen_for_qa(
            self,
            qa:QA,
            start_from:StartFrom=StartFrom.beginning,
            b_missing_only:bool = True,
            only_llms:list[str] = None
    ):
        """
        Method to be implemented to generate Answer, Fact and Eval
        """
        raise NotImplementedError('Must implement this!')

