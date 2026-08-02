# Research Protocol v0.1

## 1. Title

**Bayesian Artificial Intelligence on the Predictive Simulation of Uncertainty in Citizen Insecurity Scenarios in Lima Metropolitana, 2027**

This research proposes the development of an Artificial Intelligence model based on Bayesian Deep Learning and Generative AI to predict and simulate citizen insecurity scenarios under uncertainty. The study focuses on Lima Metropolitana as a representative urban environment facing increasing public security challenges.

---

## 2. Abstract

Citizen insecurity is one of the most significant social challenges affecting quality of life, governance, and sustainable urban development in Peru and Latin America. Current public security systems are largely reactive and provide limited support for proactive decision-making.

This study proposes a Bayesian Artificial Intelligence framework integrating Bayesian Deep Learning and Generative AI to predict criminal incidents and simulate insecurity scenarios under uncertain conditions. The proposed artifact will be evaluated through predictive performance, uncertainty estimation, and practical usefulness for public security decision-making.

---

## 3. Introduction and Problem Statement

Citizen security management in Peru faces increasing challenges due to the growing complexity and diversity of security-related incidents, including crime, urban violence, cyber threats, and emerging risks. These incidents generate significant social and economic losses and, in many cases, result in the loss of human lives. During recent months, the Peruvian government has declared states of emergency in Lima and Callao in response to the substantial increase in criminal activities and public insecurity.

According to the National Institute of Statistics and Informatics (INEI), approximately 80.9% of Peruvians who have been victims of crime do not report these incidents to the authorities, highlighting a significant gap between actual and recorded crime rates. Additionally, the Public Prosecutor's Office has reported numerous victims associated with criminal incidents occurring within the public transportation system, reflecting the severity of the current security situation.

At the same time, encouraging efforts have emerged to promote data transparency and accessibility through open data initiatives provided by institutions such as the National Police of Peru (PNP), INEI, and public security observatories. These data sources offer valuable opportunities for advanced analytics and the development of Artificial Intelligence (AI)-based decision-support systems. Furthermore, the Peruvian government has invested in intelligent surveillance infrastructure, including AI-enabled cameras and integrated monitoring centers, aiming to strengthen crime prevention and response capabilities. However, the effectiveness of these initiatives depends on the availability of advanced analytical tools capable of transforming data into actionable intelligence.

Artificial Intelligence provides computational methods and predictive algorithms capable of processing large-scale heterogeneous datasets, identifying hidden patterns, forecasting future events, and generating actionable recommendations. These capabilities can support public security strategies by anticipating crime trends, identifying high-risk areas, and optimizing resource allocation. Moreover, advanced AI techniques can be used to simulate alternative security scenarios by modeling variations in the key factors influencing criminal activity, thereby supporting strategic planning and policy evaluation.

The development of an intelligent framework capable of predicting and simulating citizen security conditions would enable authorities to evaluate the impact of different intervention strategies, identify critical risk factors, and recommend preventive actions aimed at reducing security incidents. Such capabilities could significantly enhance evidence-based decision-making processes and contribute to the formulation of more effective public security policies.

Despite recent technological advancements, there is currently a lack of comprehensive solutions that integrate predictive analytics, uncertainty modeling, and scenario simulation for citizen security management. Specifically, existing systems do not adequately support:

• Predicting security incidents while explicitly considering uncertainty and associated risk factors.

• Generating simulation scenarios to evaluate preventive policies and intervention strategies before implementation.

• Providing concrete, prioritized, and actionable recommendations for government authorities and security agencies.

These limitations reduce the ability of institutions to anticipate critical events, optimize the allocation of public resources, and proactively mitigate security risks. Consequently, there is a growing need for innovative AI-based frameworks that combine predictive modeling, uncertainty quantification, and scenario generation to support strategic decision-making and strengthen citizen security in Peru and other Latin American countries facing similar challenges.


---

## 4. Literature Review

Recent advances in Artificial Intelligence have demonstrated the effectiveness of machine learning and deep learning techniques in crime prediction and urban analytics. Bayesian approaches are particularly relevant because they provide probabilistic predictions and explicit uncertainty estimation.

Generative AI has also emerged as a promising technology for scenario simulation, enabling the creation of alternative future conditions that can support strategic planning and risk assessment. However, the integration of Bayesian Deep Learning and Generative AI for citizen insecurity management remains relatively unexplored, particularly in Latin America.

Dataset will be download from INEI (Census) and Crime Open data.


### Related Studies

| ID | Authors | Year | Research Problem | Objective | Methodology / Data Sources | Main Findings | Research Gap |
|----|---------|------|------------------|-----------|----------------------------|---------------|--------------|
| P1 | Vega-Huerta et al. | 2025 | High levels of citizen insecurity in Lima and the need to anticipate crime hotspots. | To develop a mobile application capable of predicting high-crime areas using Machine Learning techniques. | Historical crime reports and geospatial crime databases. Random Forest and Gradient Boosting algorithms were employed. | Predictive models significantly improved the allocation of security resources and personnel deployment in critical areas. | The study does not quantify predictive uncertainty nor simulate alternative crime scenarios. |
| P2 | Hernández Caro et al. | 2025 | Limited effectiveness of traditional surveillance systems in responding to criminal activities in real time. | To evaluate the effectiveness of AI-powered video surveillance systems for crime prevention. | Semi-structured interviews with security operators and documentary analysis of police intervention reports. | AI-enhanced surveillance systems improved early detection of suspicious behavior and strengthened police operational capabilities. | Focuses on monitoring and detection rather than predictive modeling and uncertainty estimation. |
| P3 | Mandalapu et al. | 2023 | Need for more accurate crime prediction models to support governmental decision-making. | To review advances in crime prediction using Deep Learning techniques. | Systematic literature review, bibliometric analysis, and comparative synthesis of scientific publications. | Probabilistic approaches and predictive scenario generation are essential for improving risk management and proactive security policies. | Does not propose an integrated framework combining Bayesian Deep Learning and Generative AI. |

---

## 5. Research Questions and Hypotheses

### Main Research Question

How can Bayesian Deep Learning and Generative AI simulate predictive uncertainty in citizen insecurity scenarios to support decision-making in Lima Metropolitana?

### Secondary Research Questions

1. How can Bayesian Deep Learning improve the prediction of citizen insecurity incidents in Lima Metropolitana?
2. To what extent can Generative AI support the simulation of future crime scenarios?
3. How can uncertainty estimation improve public security decision-making?

### Hypothesis

The integration of Bayesian Deep Learning and Generative AI will improve predictive performance and provide meaningful uncertainty-aware simulations that support decision-making in public security management.

---

## 6. Methodology


This research adopts a **Design Science Research (DSR)** methodology within a **positivist research paradigm**. The study aims to design, develop, and evaluate an Artificial Intelligence artifact capable of supporting strategic decision-making for citizen security management in Lima Metropolitana. The proposed artifact integrates **Bayesian Deep Learning** and **Generative Artificial Intelligence** to predict crime incidents, quantify uncertainty, simulate alternative security scenarios, and generate actionable recommendations for public authorities.

The DSR process will be structured according to the following phases: **problem identification and motivation**, **definition of research objectives**, **artifact design and development**, **demonstration**, **evaluation**, and **communication of results**. This approach ensures that the research not only contributes to scientific knowledge but also provides a practical solution to a real-world societal challenge.

The research will follow **Open Science and Reproducible AI principles**. All experiments, datasets, model versions, and pipelines will be managed using **Git** for version control, **DVC (Data Version Control)** for data lineage and reproducibility, **Docker** for environment standardization, and **MLflow** for experiment tracking, model lifecycle management, and performance monitoring. These practices will ensure transparency, reproducibility, scalability, and scientific rigor throughout the research lifecycle.

---

## 7. Ethical Considerations

This project will use exclusively secondary, aggregated public datasets from Peruvian government institutions (such as INEI and SISPOL), without involving human subjects or personally identifiable information. The study prioritizes transparency, explainability via uncertainty intervals, and strict human oversight to mitigate ethical risks such as algorithmic bias or geographic stigmatization, ensuring the system functions solely as a decision-support tool guided by national and international ethical principles.


---

## 8. Expected Results

The study is expected to produce a Bayesian Artificial Intelligence framework capable of predicting citizen insecurity incidents and simulating alternative future scenarios under uncertainty.

Expected outputs include a predictive model, a simulation component based on Generative AI, an uncertainty estimation mechanism, and a reproducible AI pipeline. The framework should contribute both academically and practically to public security management.

---

## 9. Timeline and Budget

The research is expected to be completed during the doctoral program period through iterative Design Science cycles.

### Tentative Timeline

| Phase  | Activities                                                |
| ------ | --------------------------------------------------------- |
| Year 1 | Literature review, protocol development, data acquisition |
| Year 2 | Artifact design and model development                     |
| Year 3 | Evaluation, validation, refinement, thesis writing        |

### Budget Considerations

The project primarily requires computational resources, cloud services, software tools, and access to public security datasets. Existing institutional infrastructure is expected to support most research activities.

---

## 10. Bibliography

Baskerville, R., & Pries-Heje, J. (2010). Explanatory Design Theory.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design Science in Information Systems Research.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning.

Murphy, K. P. (2023). Probabilistic Machine Learning: Advanced Topics.

Russell, S., & Norvig, P. (2021). Artificial Intelligence: A Modern Approach.

UNODC. (2024). Crime and Criminal Justice Statistics.

World Bank. (2024). Urban Security and Governance Indicators.



