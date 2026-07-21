from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")
    # print(os.getenv("OPENAI_API_KEY"))
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 10, 2026, Forbes estimates his net worth to be US$797 billion.

Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded Zip2, a web software company. Following its sale in 1999, he co-founded X.com, an e-commerce payment system that merged with Confinity in March 2000 to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.

Musk is the founder, CEO, and chief engineer of SpaceX; early in his career, he was also involved in the companies Zip2 and X.com, which provided business-to-business web portal software to corporate clients. He was then involved in the companies PayPal and Tesla, Inc., which aimed to develop electric vehicles and batteries, with the latter being his most successful project to date. Musk has promoted sustainable energy and has advocated for the shift from fossil fuels to electric vehicles. He has been criticized for unorthodox or controversial stances and public behavior, and for making unsubstantiated claims.

Musk was born to a Canadian mother and South African father, and raised in Pretoria, South Africa. He briefly attended the University of Pretoria before moving to Canada aged 17 to attend Queen's University. He transferred to the University of Pennsylvania two years later, where he received a Bachelor of Science degree in physics and a Bachelor of Arts degree in economics. He moved to California in 1995 to attend Stanford University but decided to instead pursue a business career, co-founding the web software company Zip2 with his brother Kimbal. The startup provided business-to-business web portal software to corporate clients. The company grew rapidly and gained a significant market share in the market for online business-to-business directories, and Musk, its CEO, received substantial personal compensation as a result. The company went public in 1999 and generated over US$22 million in revenue during its first year.

In 1999, Musk co-founded X.com, an online financial services and electronic payment company. Eight years later, the company became the largest online payment system in the world, and was renamed PayPal. In 2002, eBay acquired PayPal for US$1.5 billion in stock, and Musk received US$165 million for his 11% share. Two years later, he helped to found SpaceX, an aerospace manufacturer and space transport services company, and became its CEO and chief engineer. In 2008, he helped to establish Tesla Motors, Inc., an electric vehicle manufacturer, and became its CEO and product architect. In 2004, he joined the investment bank Goldman Sachs to advise it on renewable energy development.

In 2015, Musk unveiled the Hyperloop, a high-speed transportation system concept. Also in 2015, he co-founded OpenAI, a nonprofit research company focused on artificial intelligence (AI). In July 2016, he co-founded Neuralink, a neurotechnology company focused on developing brain–computer interfaces, and is its CEO and chief technology officer. In August 2016, he announced a proposed scheme to colonize the planet Mars. In 2020, Musk founded The Boring Company, a tunnel construction company focused on developing tunnels for transportation and logistics. In May 2021, he was named one of Time's 100 most influential people in the world.
    """
    summary_template = """
Summarize the following information:
{information}
"""
    summary_prompt = ChatPromptTemplate.from_template(summary_template)

    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    chain = summary_prompt | llm
    result = chain.invoke({"information": information})
    print(result.content)


if __name__ == "__main__":
    main()
