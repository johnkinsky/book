
Documentation Analytics and Analysis
=====================================

It’s important to understand that documentation analytics are a special case when presenting information; in fact, most analytical or behavioral tools one uses for documentation analytics are borrowed from another discipline. It’s impossible to use current analytics tools and methods without first adapting them. 

First, some basic working definitions of analytics and analysis. When I use these terms, I mean. 

- Analytics – Using descriptive, inferential, or predictive statistical methods to examine, transform, model, and prepare data for analytic analysis.
- Analysis – Explaining and visualizing the results of the analytic work. Providing insights arising from analytic process to drive business or content decisions. 

.. Note:: Examples of common web analytics platforms are Adobe Analytics or Adobe Customer Journey Analytics and Google Analytics 4. Common behavioral analytics platforms are hotjar, Microsoft Clarity, Contentsquare, and Siteimprove. In all cases, the assumed audience for the data and insight is marketing or web administrators, so the data is reported in terms of return on investment, ad spending, or site health. I will cover both types of analytics platforms, highlight some uses, and provide some examples in the future.

Most documentation whether web based or merely downloaded from the web consists of multiple topics (sometimes hundreds or thousands of topics) in separate sections notionally connected by UI/UX designs as a unitary whole. Simple page or journey analysis practices borrowed from marketing or administration are not sufficiently complex to fulfill documentation analysis needs.

Unlike typical data analytics, web analytics, or behavioral analytics, documentation analytics data must be aggregated and contextualized before analysis or any insights are possible. Attaching web property analytics to documentation leads to bad analysis. One example is bouncing rates. 

In the past, even Google stated that bounce rates should be analyzed in the context of the type of content (https://support.google.com/analytics/answer/1009409). 

Bounce rates are high, or low are one of the numbers stakeholders I’ve worked with have focused on trying to fix without understanding some fundamentals. A bounce is often understood to describe a single session or visit to a page on a web site, or some other property, with no further interaction on the site, regardless of the time spent on the page. For marketing, this is alarming user behavior; a user who visits a page but does not transit to another page on the same site, request more information, or purchase something is a lost opportunity.

The bounce rate is calculated percentage of times that kind of behavior occurred when compared against all sessions or visits for a specific period. For example, assume you had 100 visits/session in a week. Of the 100 visits/sessions, 60 visits/sessions included users who viewed a single page, did nothing else and left. That’s a bounce rate of 60% for the week. Marketing folks would panic with a bounce rate that high. 

That model does not apply to documentation. Finding the proper bounce rate for documentation requires that the analytics and analysis starts with two contextual constraints:

- Documentation type – Different content types might have different expected user behaviors. 
- User acquisition – Different sources and channels might have different expected behaviors.

Before one can analyze the data, one must know something about the content type and how the user first encountered the content. For example, consider the following scenarios. 

- **Scenario 1.** A self-contained reference topic that did not require reading any other topic to provide detailed, actionable information might be expected to have high bounce rate if the user came to the page, got a useable answer to a specific question, and moved on to productive work.  A high bounce rate on a particular topic, and similar topics in the same document, could be a sign of success. A low bounce rate might indicate failure if the user continued to similar topics or pages before leaving. 
- **Scenario 2.** An installation topic might be expected to have a relatively low bounce rate if the topic did not have all necessary information to complete all installation steps. If a user viewed the topic and did not to move to another topic in the same document or on any page on the site, then a high bounce rate is probably a sign of failure. A low bounce rate might show success if the user next visited a page in the expected workflow or a page that included information that could reasonably be connected to the original page. 

For software documentation available from a web site, it’s an almost universal truth that something like 60%, or more, of traffic to software documentation comes from Google search. 

Suppose users came to documentation in both scenarios from user-initiated searches (organic searches), and the web analytics data showed that organic searches resulted in high-bounces rates for both types of topics. 

Suppose further the web analytics showed that significant traffic in both scenarios came from direct traffic (or bookmarks which are email links, links saved in a web browser, or links from the same site) and they also showed high bounce rates. 

Suppose that web analytics traffic shows that users viewing the content from browsers on mobile devices match your initial expectations (scenario 1 = low bounce rates, scenario 2 = high bounce rates), but data show that users viewing from desktop browsers displayed the opposite behavior (scenario 1 = high bounce rates, scenario 2 = low bounce rates).

In what ways should these considerations affect analysis? 

This is a simplified explanation of often used metric in many companies. In newer analytics platforms, bounces are redefined to include site visits or sessions with no substantial user engagement (https://support.google.com/analytics/answer/12195621); in some definitions high engagement implies a user stayed on the page/topic for a predetermined time, viewed more than a single page, or followed a specific content path. The definition might have changed, but the essential need to contextualize the analytics and analysis hasn’t changed since the beginning of the internet.

Web Analytics
=============================================

- Adobe Analytics - https://business.adobe.com/products/adobe-analytics.html
- Adobe Customer Journey Analytics - https://business.adobe.com/products/adobe-analytics/customer-journey-analytics.html
- Google Analytics 4 - https://support.google.com/analytics/answer/10089681

Behavioral Analytics
=============================================

- Microsoft Clarity - https://clarity.microsoft.com
- hotjar (ContentSquare) -https://www.hotjar.com
- Siteimprove - https://www.siteimprove.com

Data Transformation and Visualization 
=============================================

Listed in order from from simple to complex.

- OpenOffice Calc -  https://www.openoffice.org/product/calc.html
- Microsoft Excel  - https://support.microsoft.com/en-us/office/what-is-excel-94b00f50-5896-479c-b0c5-ff74603b35a3
- Power BI Desktop - https://www.microsoft.com/en-us/power-platform/products/power-bi/desktop
- Python (pandas and matplotlib) - https://pypi.org/project/pandas/ and https://pypi.org/project/matplotlib/
