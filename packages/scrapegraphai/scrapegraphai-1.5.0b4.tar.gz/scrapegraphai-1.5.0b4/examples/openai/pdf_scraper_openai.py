""" 
Basic example of scraping pipeline using PDFScraper
"""

import os
from dotenv import load_dotenv
from scrapegraphai.graphs import PDFScraperGraph

load_dotenv()


# ************************************************
# Define the configuration for the graph
# ************************************************

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key":openai_key,
        "model": "gpt-3.5-turbo",
    },
    "verbose": True,
    "headless": False,
}

# Covert to list
sources = [
    "This paper provides evidence from a natural experiment on the relationship between positive affect and productivity. We link highly detailed administrative data on the behaviors and performance of all telesales workers at a large telecommunications company with survey reports of employee happiness that we collected on a weekly basis. We use variation in worker mood arising from visual exposure to weatherâ€”the interaction between call center architecture and outdoor weather conditionsâ€”in order to provide a quasi-experimental test of the effect of happiness on productivity. We find evidence of a positive impact on sales performance, which is driven by changes in labor productivity â€“ largely through workers converting more calls into sales, and to a lesser extent by making more calls per hour and adhering more closely to their schedule. We find no evidence in our setting of effects on measures of high-frequency labor supply such as attendance and break-taking.",
    "The diffusion of social media coincided with a worsening of mental health conditions among adolescents and young adults in the United States, giving rise to speculation that social media might be detrimental to mental health. In this paper, we provide quasi-experimental estimates of the impact of social media on mental health by leveraging a unique natural experiment: the staggered introduction of Facebook across U.S. colleges. Our analysis couples data on student mental health around the years of Facebook's expansion with a generalized difference-in-differences empirical strategy. We find that the roll-out of Facebook at a college increased symptoms of poor mental health, especially depression. We also find that, among students predicted to be most susceptible to mental illness, the introduction of Facebook led to increased utilization of mental healthcare services. Lastly, we find that, after the introduction of Facebook, students were more likely to report experiencing impairments to academic performance resulting from poor mental health. Additional evidence on mechanisms suggests that the results are due to Facebook fostering unfavorable social comparisons.",
    "Hollywood films are generally released first in the United States and then later abroad, with  some variation in lags across films and countries. With the growth in movie piracy since the appearance of BitTorrent in 2003, films have become available through illegal piracy immediately after release in the US, while they are not available for legal viewing abroad until their foreign premieres in each country. We make use of this variation in international release lags to ask whether longer lags â€“ which facilitate more local pre-release piracy â€“ depress theatrical box office receipts, particularly after the widespread adoption of BitTorrent. We find that longer release windows are associated with decreased box office returns, even after controlling for film and country fixed effects. This relationship is much stronger in contexts where piracy is more prevalent: after BitTorrentâ€™s adoption and in heavily-pirated genres. Our findings indicate that, as a lower bound, international box office returns in our sample were at least 7% lower than they would have been in the absence of pre-release piracy. By contrast, we do not see evidence of elevated sales displacement in US box office revenue following the adoption of BitTorrent, and we suggest that delayed legal availability of the content abroad may drive the losses to piracy."
    # Add more sources here
]

prompt = """
You are an expert in reviewing academic manuscripts. Please analyze the abstracts provided from an academic journal article to extract and clearly identify the following elements:

Independent Variable (IV): The variable that is manipulated or considered as the primary cause affecting other variables.
Dependent Variable (DV): The variable that is measured or observed, which is expected to change as a result of variations in the Independent Variable.
Exogenous Shock: Identify any external or unexpected events used in the study that serve as a natural experiment or provide a unique setting for observing the effects on the IV and DV.
Response Format: For each abstract, present your response in the following structured format:

Independent Variable (IV):
Dependent Variable (DV):
Exogenous Shock:

Example Queries and Responses:

Query: This paper provides evidence from a natural experiment on the relationship between positive affect and productivity. We link highly detailed administrative data on the behaviors and performance of all telesales workers at a large telecommunications company with survey reports of employee happiness that we collected on a weekly basis. We use variation in worker mood arising from visual exposure to weather the interaction between call center architecture and outdoor weather conditions in order to provide a quasi-experimental test of the effect of happiness on productivity. We find evidence of a positive impact on sales performance, which is driven by changes in labor productivity largely through workers converting more calls into sales, and to a lesser extent by making more calls per hour and adhering more closely to their schedule. We find no evidence in our setting of effects on measures of high-frequency labor supply such as attendance and break-taking.

Response:

Independent Variable (IV): Employee happiness.
Dependent Variable (DV): Overall firm productivity.
Exogenous Shock: Sudden company-wide increase in bonus payments.

Query: The diffusion of social media coincided with a worsening of mental health conditions among adolescents and young adults in the United States, giving rise to speculation that social media might be detrimental to mental health. In this paper, we provide quasi-experimental estimates of the impact of social media on mental health by leveraging a unique natural experiment: the staggered introduction of Facebook across U.S. colleges. Our analysis couples data on student mental health around the years of Facebook's expansion with a generalized difference-in-differences empirical strategy. We find that the roll-out of Facebook at a college increased symptoms of poor mental health, especially depression. We also find that, among students predicted to be most susceptible to mental illness, the introduction of Facebook led to increased utilization of mental healthcare services. Lastly, we find that, after the introduction of Facebook, students were more likely to report experiencing impairments to academic performance resulting from poor mental health. Additional evidence on mechanisms suggests that the results are due to Facebook fostering unfavorable social comparisons.

Response:

Independent Variable (IV): Exposure to social media.
Dependent Variable (DV): Mental health outcomes.
Exogenous Shock: staggered introduction of Facebook across U.S. colleges.
"""

pdf_scraper_graph = PDFScraperGraph(
    prompt=prompt,
    source=sources[0],
    config=graph_config
)
result = pdf_scraper_graph.run()


print(result)
