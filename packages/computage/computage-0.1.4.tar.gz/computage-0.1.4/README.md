# ComputAge
A library for full-stack aging clocks design and benchmarking.

*The full release version of the package is currently developing. Only bechmarking module is released and ready for use. Please see below.*

## Installation

You can install the whole library with `pip`:

`pip install computage`

This provides all necessary instruments for aging clocks benchmarking.

# ComputAgeBench

A module in the `computage` library for epigenetic aging clocks benchmarking. This library is tightly bound with `computage_bench` huggingface [repository](https://huggingface.co/datasets/computage/computage_bench) where all DNA methylation data can be retrieved from. All details on our methodology of epigenetic aging clocks benchmarking and results can be found in the paper [...upcoming...].

## Introduction

**DNA methylation** is a chemical modification of DNA molecules that is present in many biological species, including humans. 
Specifically, methylation most often occurs at the cytosine nucleotides in a so-called **CpG context** (cytosine followed by a guanine). 
This modification is engaged in a variety of cellular events, ranging from nutrient starvation responses to X-chromosome inactivation to transgenerational inheritance. 
As it turns out, methylation levels per CpG site change systemically in aging, which can be captured by various machine learning (ML) models called **aging clocks** 
and used to predict an individual’s age. Moreover, it has been hypothesized that the aging clocks not only predict chronological age, but can also estimate 
**biological age**, that is, an overall degree of an individual’s health represented as an increase or decrease of predicted age relative to the general population. 
However, comparing aging clock performance is no trivial task, as there is no gold standard measure of one’s biological age, so using MAE, Pearson’s *r*, or other 
common correlation metrics is not sufficient.

To foster greater advances in the aging clock field, [we developed a methodology and a dataset](https://huggingface.co/datasets/computage/computage_bench) for aging clock benchmarking, ComputAge Bench, which relies on measuring 
model ability to predict increased ages in samples from patients with *pre-defined* **aging-accelerating conditions** (AACs) relative to samples from 
healthy controls (HC). **We highly recommend consulting the Methods and Discussion sections of our paper before proceeding to use this dataset and to build 
any conclusions upon it.**

<p align="center">
<img src="images/fig1.png" alt>

</p>
<p align="center">
<em>ComputAgeBench epigenetic clock construction overview.</em>
</p>

## Usage (benchmarking)

### sklearn-based model

Suppose you trained brand-new epigenetic aging clocks model using classic `scikit-learn` library. You saved your model as `pickle` file. Then, the following block of code can be used for benchmarking your model. We also added several other published aging clocks for comparison with yours.
```python
from computage import run_benchmark

#first define NaN imputation method for in_library models
#for simlicity here we recommend to use imputation with zeros
imputation = 'none'
models_config = {
    "in_library":{
        'HorvathV1':{'imputation':imputation},
        'Hannum':{'imputation':imputation},
        'PhenoAgeV2':{'imputation':imputation},
				},
	#here we should define a name of our new model as well as path
    #to the pickle file (.pkl) of the model
    "new_models":{
        #'my_new_model_name': {'path':/path/to/model.pkl}
        }
}
#now run the benchmark
bench = run_benchmark(models_config, 
        experiment_prefix='my_model_test',
        output_folder='./benchmark'
        )
#upon completion, the results will be saved in the folder you specified
```
### pytorch-based model
[...upcoming...]

## Reproducing paper results


## Cite us
[...coming soon...]


## Contact

For any questions or clarifications, please reach out to: dmitrii.kriukov@skoltech.ru

## Acknowledgments




