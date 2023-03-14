# iacreview

This is the replication package for the paper institled "Code Review Practices for Infrastructure-as-Code: An
Empirical Study on OpenStack Projects". 

Infrastructure-as-code (IaC) allows the automatic management and provisioning of infrastructures using machine-readable specification files. Consequently, developers are able to apply quality assurance practices, such as the code review on the IaC code files.

This paper investigates the code review practices of IaC-related code changes compared to Non-IaC code changes in terms of 10 code review related attributes ( ``number of reviewers``, `` number of revisions``, ``review duration``, `` number of files``, ``churn``, ``added lines``, ``deleted lines``, ``code change description length``, ``number of inline-comments``, and ``number of exchanged messges``). 


In this repository, we provide,

1) The script used to [``fetch the code review data from the review platform``](https://github.com/stilab-ets/iacreview/blob/main/Scripts/Fetch_OpenStack_Code_Review_Data.ipynb) and other custom scripts.
2) The fetched [``code review data for the OpenStack ecosystem``](https://github.com/stilab-ets/iacreview/tree/main/OpenStack_Code_Review_Data) from 2014 to 2021.
3) The data for [``the code review attributes per release``](https://github.com/stilab-ets/iacreview/tree/main/Code_Review_Attributes_Data_Per_Release) from the Kilo release till Victoria release for both IaC and Non-IaC code changes. 
4) The data for [``the code review attributes per phase``](https://github.com/stilab-ets/iacreview/tree/main/Code_Review_Attributes_Data_Per_Phase). For each release, we provide the code review attributes for the ``development`` (dev) phase, the ``release-candidate`` (RC) phase, and the ``post-release`` (PR) phase.  
