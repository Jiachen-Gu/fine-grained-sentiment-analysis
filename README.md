# Airbnb users' sentiments through topic modeling and sentiment analysis
The advent of technology and rapid digitalization of businesses have opened up many possibilities for companies. One of the products of the digitalization is sharing accommodation, which is a concept that was made popular by Airbnb. As the market leader in the sharing accommodation industry, it has established itself as a notable opponent to the traditional hotel chains as an increasing number of travellers have converted to choose the accommodation provided by Airbnb over hotels due to the more competitive pricing. However, the status of the company as the pioneer and market is not unchallenged, given the fact there are few newer companies who have joined the market. Aside from the increased competition, the company is also facing a long-term issue, which is the safety and credibility of their listings. Particularly, the actual quality of the accommodation and services remains one of the biggest hindrances for the company to overcome. Although the company has implemented a review system, the system’s reliability is heavily questioned due to the severe positive bias found in the reviews. And because of the positive bias, the company may not be able to recognize the actual customer experiences and area for improvement, which will eventually lead to the company stagnating. Therefore, the current study has analysed the reviews about Airbnb from two different platforms using topic modelling and fine-grained sentiment analysis to provide a more objective view of the Airbnb customers’ experience. The findings revealed that the positive bias is still present in the reviews of Airbnb. Furthermore, customers from the two platforms are mentioning very different issues and have expressed very different sentiments towards the various aspects of Airbnb. Based on the findings, several recommendations were proposed for the company to further improve their understanding of the customers’ experience.

## Significance of the project
Aside from hindering the company’s ability to improve, the lack of negative or neutral comments have also indirectly led to the lack of research conducted in this regard. So far, majority of the studies conducted have focused primarily at the positive reviews (Hu, Zhang, Pavlou, 2009). Although a pioneering study on negative comments of Airbnb was conducted by Sthapit and Bjork (2019), the researchers have chosen the qualitative methods where only major themes were extracted from the negative comments collected. Although the study has provided some guidance in regard to the dissatisfaction experienced by customers of Airbnb, the study did not indicate the extent of the customers dissatisfaction on various aspects of Airbnb’s service. By performing an in-depth analysis on the comments of the Airbnb guests, the current project may provide contribution in both the research community and the business context. Specifically, the findings may demonstrate the advantages of using data analytics techniques in understanding customers experience. Furthermore, the fine-grained sentiment analysis technique chosen will also provide greater nuances in terms of indicating the extent of customers’ emotion polarity. By making use of the findings, the company will be able to understand the true experiences of the customers and rectify aspects that the company is lacking. 

## Methods
1. Web scraping from trustpilot and airbnb with beautiful soup (academic purposes)
2. Data exploration - data quality and visualization
3. Data pre-processing - lower cases, data cleaning if required.
4. Expect Extraction - LDA
5. Aspect Sentiment Analysis
6. Result.

## How to run ipynb file

```bash
pip install -r requirement.txt
jupyter lab 
```

## How to run the python file

```
1. Perform web scrapping from airbnb and trust pilot, running webscrapping/main.py 
  1. To avoid iterative process, developer can choose to perform scrapping with RPA
  
2. Using airbnb/Topic Modelling.ipynb to run the lda model and create file "original_imbalanced_predictive_model.csv"
  1. In order to treat the class imbalanaced issue on the dataset we have, we run sampling treatement to our model.
  2. Then we perform logistic regression at the evaluation part to evaluate our model.
  3. Running "LexiconBased in Airbnb.ipynb" complimenting with lbsa.py for sentiment analysis.

3. Repeat step 2 on trust pilot data

4. Running wordcloud to perform analysis

```
