from master.agent import Researcher
import asyncio

async def get_report(query: str, report_type: str) -> str:
    researcher = Researcher(query, report_type)
    report = await researcher.conduct_research()
    return report

if __name__ == "__main__":
    query = "what day is today?"
    report_type = "research_report"

    report = asyncio.run(get_report(query, report_type))
    print(report)