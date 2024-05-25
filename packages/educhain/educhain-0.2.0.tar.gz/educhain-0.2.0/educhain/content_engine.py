from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def generate_lesson_plan(subject, level, llm=None):

    if llm:
        llm = llm
    else:
        llm = ChatOpenAI(model = 'gpt-3.5-turbo-0125')

    prompt = PromptTemplate(
        input_variables=["subject", "level"],
        template="""
    Generate a lesson plan for the given subject and level.
    Provide a detailed outline of the lesson, including an introduction, main activities, and a conclusion.

    Subject: {subject}
    Level: {level}

    Lesson Plan:
    """,
    )

    # Create an LLMChain using the prompt and ChatOpenAI
    lesson_plan_chain = LLMChain(llm=llm, prompt=prompt)

    # Generate the lesson plan
    lesson_plan = lesson_plan_chain.predict(subject=subject, level=level)

    return lesson_plan