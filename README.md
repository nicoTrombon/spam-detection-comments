# spam-detection-comments
Algorithm for detection of spam in Youtube video comments

# How to use
```
git clone https://github.com/nicoTrombon/spam-detection-comments.git
cd spam-detection-comments
virtualenv .venv
source .venv/bin/activate
pip install requirements.txt
python classifier.py
```

# Results
```
Predictions for some examples
**********
Example: ['z13ttr3z1kybet3io04cfv2icvbtj3ro120' 'ZRSFirelordGaming'
 '2015-05-16T18:17:34.524000'
 'XD I WAS GOING CRAZY FUCKIN CRAZY WATCHIN THIS BRAH\xef\xbb\xbf']
Expected result: 0
Prediction: 0
**********
Example: ['z12tclby1nuyflgbw04cdnyg3zfvefn5lrg0k' 'Technibility'
 '2014-09-12T21:08:47'
 'Great video by a great artist in Katy Perry! Admire her creativity! Check  out our channel for no nonsense mobile tech reviews and comparisons as well  as an iPhone 6 and 6 Plus review and comparison!\xef\xbb\xbf']
Expected result: 1
Prediction: 1
**********
Example: ['z13pitkr5prbgf3ja04cjjg4qme3txjpyqc0k' 'Yeung Marvin'
 '2014-11-12T23:56:54'
 'Haha its so funny to see the salt of westerners that top views of youtube  goes to video they dont even understand, keep the salt up!\xef\xbb\xbf']
Expected result: 0
Prediction: 0
**********
Example: ['z13ighawfwy5y5t5a04ccnp5dozetzfpq0g' 'Snipe Last' '2014-09-22T19:34:46'
 'why the elephant have a broken horn\xef\xbb\xbf']
Expected result: 0
Prediction: 0
**********
Example: ['z13xjfr42z3uxdz2223gx5rrzs3dt5hna' 'Jihad Naser' ''
 'Hello I&#39;am from Palastine\xef\xbb\xbf']
Expected result: 1
Prediction: 0
```
