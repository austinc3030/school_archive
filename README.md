# Final Project Pt 1
We estimate it will take:

    6 hours to generate the design document
    8 hours to generate unit tests
    12 hours for implementation of the requirements split as follow:
        6 hours for Requirement 1 (REQUIRED) – Want all localization capability done in one library.
        0 hours for Requirement 2 (DESIRED) – The ability to switch locales during execution.
        0 hours for Requirement 3 (DESIRED) – Merge po files together.
        0 hours for Requirement 4 (DESIRED) – Have xtext run as part of build process – VS pre-build or post build step
        6 hours for Requirement 5 (REQUIRED) – Have library be in “core” layer but separate from libcore
        0 hours for Requirement 6 (DESIRED) – Have utilities that checks for mo files (or find where boost says where it is looking)

 

For estimating the introduction of localization into an existing project, we believe the estimate would be better refined after spending time to develop the design documentation. With the design documentation created, we will have a better understanding of the existing codebase leading to a better indication on the level of effort that will be required.

# Original Readme Contents Below
## SoftwareArchitectureCLassApplication
This is sandbox code to show proof of concept usages of some principles taught in University of Cincinnati's Software Architecture Class.

This code base will be used for several assignments, but it's value comes from having several libraries in play, as well as some example usages of concepts of singletons, static initializers, journaling, and automation APIs

Additionally, this also shows how to setup a Basic Action to verify a merge request compiles or not.


This software to show off some workflows with using Java and automation APIs depends upon a Java Provider to present.  Otherwise a build error will occur.

To Resovle this install a Java JDK (such as Adopt OpenJDK), and then provide the proper header includes and library location.  It is being proposed as future enhancment to make the jvm library be loaded dyanmically.

Or optionally comment out the code in PerformJavaAutomationWorkflow, and turn off building the JavaLoader library.

[Journaling Module Design](documentation_markdown/journaling.md)
