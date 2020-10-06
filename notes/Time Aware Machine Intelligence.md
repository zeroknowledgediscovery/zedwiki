# AIM

**a self awareness of the complex time-conditioned property of neural networks’ knowledge encoding**

# Overview


+ https://research.ibm.com/artificial-intelligence/publications/paper/?id=Patient-Subtyping-via-Time-Aware-LSTM-Networks
+ https://arxiv.org/abs/1911.09431
+ https://ieeexplore.ieee.org/abstract/document/8904698
+ https://sociable.co/technology/darpa-making-ai-self-aware-time-dimensions/


# The Challenge

+ Current neural networks do not explicitly model the inherent time characteristics of their encoded knowledge.
+ Consequently, state-of-the-art machine learning does not have the expressive capability to reason with encoded knowledge using time.

# The Proposed Solution

+ TAMI’s vision is for an AI system to develop a detailed self-understanding of the time dimensions of its learned knowledge and eventually be able to “think in and about time” when exercising its learned task knowledge in task performance.

+ Consider neural networks designed for inference. Such neural networks derive abstract task knowledge from the analysis of a large number of data samples.

+ Each data sample exists only in a specific time. For example, features given by a vehicle data sample are associated with that specific vehicle’s age (e.g., rust and dents) and, therefore, are explicitly dependent on time.

+ Neural networks incorporate such information as static activation weights; however, using the example above, the activation of these weights should ideally be conditioned on time.