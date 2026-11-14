# Heredity

This project estimates the probability that each person has 0, 1, or 2 copies of a gene and the probability that they express a related trait. It uses a Bayesian model to combine observed traits, family relationships, gene inheritance, and mutation.

## Problem statement

Given a CSV file listing people, their parents, and any known trait observations, calculate a probability distribution for each person's gene count and trait status. People without listed parents use the population gene probabilities. For children, each parent passes one gene copy, with a chance of mutation. The model combines those inheritance probabilities with the probability of the trait for each gene count, sums over possible assignments consistent with the observations, and normalizes the resulting distributions.

The implementation completes three functions:

- `joint_probability`: computes the probability of a particular assignment of gene counts and traits across the family.
- `update`: adds that joint probability to each person's gene and trait distributions.
- `normalize`: scales each distribution so its values sum to 1 while preserving their relative proportions.

The complete assignment description and examples are available in the [CS50 AI Heredity project specification](https://cs50.harvard.edu/ai/projects/2/heredity/).

## Run

```bash
python heredity.py data/family0.csv
```
