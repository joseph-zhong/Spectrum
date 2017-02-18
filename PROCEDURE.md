# Features

Features used for political spectrum analysis

## Summary

We first took from [this graphic](spectrum.jpg) as a baseline guide to
begin with.

We then built a corpus of the the various news sources by scraping the
websites for articles and downloading the article body.

We used the IBM Watson's [Tone Analyzer](#IBM-Watson-Tone-Analyzer)
to extract the relevant metrics which we will use to map to the
political spectrum.

We then took the features as the elements for the decision tree to
define the political spectrum of where each article generally stands

## IBM Watson Tone Analyzer

See official [documentation](https://www.ibm.com/watson/developercloud/doc/tone-analyzer/index.html)

### Document-level Analysis
```
< .5 = not likely present
> .5 = likely present
> .75 = very likely present
```
#### Emotion
- Anger
- Disgust
- Fear
- Joy
- Sadness

#### Language Style
- Analytical
- Confident
- Tentative

#### Social Tendencies
- Openness
- Conscientiousness
- Extraversion
- Agreeableness
- Emotional Range
