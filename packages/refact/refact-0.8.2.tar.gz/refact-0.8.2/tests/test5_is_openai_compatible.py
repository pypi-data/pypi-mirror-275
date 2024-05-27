import openai
import asyncio

aclient = openai.AsyncOpenAI(
    base_url="http://127.0.0.1:8001/v1",
    #base_url="https://openrouter.ai/api/v1",
    #api_key=os.getenv("OPENAI_API_KEY"),
)


initial_messages = [
("user", "Look up definition of \"Frog\" and summarize it in 5 words."),
]

async def ask_chat(messages):
    gen = await aclient.chat.completions.create(
        model="gpt-3.5-turbo",
        n=1,
        messages=[{"role": x[0], "content": x[1]} for x in messages],  # type: ignore
        temperature=0.1,
        stream=True,
    )
    content = ""
    async for g in gen:
        print(g)
        delta = g.choices[0].delta
        if delta is not None and hasattr(delta, 'content'):
            content += delta.content
            # print(delta.content, end='')  # Print the delta content as it arrives
    print()
    print("assistant says: %s" % content)


async def example_single_response():
    messages_back = await ask_chat(initial_messages)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example_single_response())
