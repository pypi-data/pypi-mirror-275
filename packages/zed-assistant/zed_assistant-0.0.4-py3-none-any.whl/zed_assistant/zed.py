import os
from logging import Logger

from openai import AsyncOpenAI

from zed_assistant.model.command_prompt import (
    CommandPromptInput,
    CommandPromptRunner,
    OperatingSystem,
)
from zed_assistant.settings.defs import ZedSettings
from zed_assistant.utils import Console


class Zed:
    def __init__(self, settings: ZedSettings, log: Logger):
        self.log = log
        self.console = Console()
        self.settings = settings
        self.command_prompt_runner = CommandPromptRunner(
            log=log,
            client=AsyncOpenAI(api_key=settings.openai_key),
            model=settings.model,
        )

    async def run(self, user_query: str) -> bool:
        """
        Main Zed executor.
        """
        self.console.show_spinner()
        cli_prompt_output = await self.command_prompt_runner.run_prompt(
            CommandPromptInput(
                input=user_query,
                operating_system=OperatingSystem.MAC_OS,
                yoda_mode=self.settings.yoda_mode,
            ),
        )
        self.console.hide_spinner()
        self.log.debug(f"Runner result: {cli_prompt_output = }")

        if not cli_prompt_output:
            self.console.print_retry()
            return False

        if cli_prompt_output.answer:
            self.console.print_answer(cli_prompt_output.answer)
        if not cli_prompt_output.command:
            return True

        self.console.print_command(cli_prompt_output.command)
        confirmed = self.console.await_confirmation()
        if confirmed:
            self.log.info(f"RUNNING {cli_prompt_output.command}")
            self.console.print_run_command(cli_prompt_output.command)
            command_result = os.system(cli_prompt_output.command)
            return command_result == 0
        else:
            self.console.print_farewell()
            return True
