# Statistics
central tendency - mean, median, mode - centre of data
median - if even = avg of n/2, n/2 + 1
        - if odd = m/2
Mean (grouped) = sum fx / sum f (x = midpoint)
        - have to estimate, not exact
model simplification - reduce variables/parameters
refining model - compare predicted data to real life data
problem solving cycle - identify problem, collect data, analyse, conclude
survey - collect info from sample of population, quicker & cheaper than census
census - collect info from every member of population, time-consuming, expensive, very accurate
sample - selection of population
systematic sampling - select every 'nth' member from list
stratified - split into categories, random selection from each
quota - specific condition selection from categories | not random
opportunity - selection convenient to sampler
simple random - every equally likely, independent selection
data - measurements with variable
qualitative - non-numerical
quantitative - numerical
discrete - categories/groups - fixed
continous - infinite range e.g weight
frequency table - discrete table data - class etc.
grouped frequency table
frequency polygon - graph, freq. against class mid-point - straight lines
Histogram - show frequencies of variables in classes - can estimate no. of readings in a given range
        - area of column = frequency
freq. density = freq. / class width
class width = upper limit - lower limit (max - min)

location - centre of data - average
linear interpolation - estimates value of variable position
dispersion - how spread out data values are
Lower Quartile - value that 25% of data is < or = (<=) - n/4 (if not integer, round UP)
Upper quartile - value that 75% of data is <= - 3n/4
        - if integer, find average of that term and next term
Interquartile range - UQ - LQ - shows range of middle 50% of data
percentile - divide data into 100
Outlier - anomaly - data outside fence range - affect what variation method to use
        - if data set has outliers, IQR is best measure
fences - the limits of data that determine whether it is an outlier
        Lower fence = Q1 - (1.5 x IQR)
        Upper fence = Q3 + (1.5 x IQR)
Standard deviation - root variance - s = ¬/``variance
Variation - how spread out data is from mean. Measures of variation:
- Standard deviation, variance, range, IQR
Cumulative frequency graph - CF goes on y-axis, plot on upper-class boundaries
Box plots - (comparing) - higher median = higher avg, higher IQR = more variation

Coding - doing an operation on every data value to simplify it

### Probability
Outcome - a possibility that can happen
Event - 'groups' of outcomes
A n B - 'intersection' - satisfy A and B || A n B == (A x B|A)
A u B - 'union' - or - satisfy either A or B
        - P(A u B) = P(A) + P(B) - P(A n B)
A' - complement A - not A
Tree diagram - show probability for 2+ events
trial - each set of branches
Conditional probability - an event GIVEN that another event has happened - B|A
B | A - probability of B, given A happened \\ B|A = A n B / A
mutually exclusive - cant happen at same time - P(A n B) = 0
        - for exclusive events, P(A u B) = P(A) + P(B)
independent events - have no effect on each other - P(A n B) = P(A) x P(B)
assumptions
X (upper) = name of random variable | random variable - no fixed value - down to chance
x (lower) = particular value that X can take
Discrete random variables - certain number of possibilities - all add up to 1
probability distribution - table showing possible values of x & probability
probability function - formula giving probabilities for different values of x
cumulative distribution function - gives probability that X <= particular value (x) (add up previous chances)
  - F(x0) = P(X <= x0) = Σp(x)
  - p(x) = P(X = x)

### Binomial distribution
- discrete
n! = amount of ways of arranging n different objects
r = number of objects that are identical
 - if r of your n objects are identical == n! / r! \\e.g ABCDA = 5! / 2! = 120 / 2 = only 60 combinations
Binomial coefficient:
 (n r) = ⁿCr = n!/r! x (n-r)!

Binomial probability function:
P(r successess in n trials) = (n r) x [P(success)]^r x [P(failure)]^n-r

Binomial distribution 5 conditions:
1) fixed number (n) of trials
2) each trial is 'success' or 'failure'
3) trials independent
4) probability is same each trial
5) variable is total number of successes in n trials
6) data also has to be discrete

Formula: P(X = x) = (n x) * p^x * (1 - p)^n-x  || X ~ B(n, p)
 - n = number of trials
 - p = probability of 'success'
 - x = number of 'successes'
### Normal distribution - 'bell shaped'
- continuous
- total area always same (1) | total area under graph = 1
- Area under graph between limit is probability of > or < that limit
- Mean is in middle, so: P(X <= mean) or P(X >= mean) = 0.5
- If X normally distributed with mean(µ) & variance(σ²), written X ~ N(µ,σ²)

- standard normal distribution Z - mean = 0, variance = 1

To convert from normal to standard normal:
1) subtract mean, then
        if X ~ N(u,o2) - X-u/o = Z, where Z ~ N(0, 1)
2) divide by standard deviation
Φ(z) - cumulative distribution function of Z 

Normal distribution conditions:
1) data continuous
2) symmetrically distributed, with peak in middle at mean(µ)
3) data less frequent as you go further from mean
4) nearly all data within 3 standard deviations of mean

Binomial: X ~ B(n, p)
Normal: X ~ N(μ, o²)


#### Normal approximation
Continuity correction:
Binomial --> normal:
P(X = b) --> P(b-0.5 < Y < b+0.5)
P(X <= b) --> P(Y < b+0.5)
P(X < b) --> P(Y < b-0.5)
P(X >= b) --> P(Y > b-0.5)
P(X > b) --> P(Y > b+0.5)
 
- works if np and n(1 - p) both > 5 