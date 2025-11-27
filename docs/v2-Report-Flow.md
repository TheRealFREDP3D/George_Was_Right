```mermaid
flowchart LR
  subgraph ContentSources
    Article[Opinion_article_on_Orwell_1984]
    Prompts[Illustration_prompts]
    Research[Research_synthesis]
    FactCheck[Fact_check_report]
  end

  subgraph RepoStructure
    LogDir[log_directory]
    ShowcaseRoot[showcases_directory]
    ShowcaseFolder[2025.NOV.26_Showcase]
    ShowcaseReport[Showcase_report_GPT_4o]
    ShowcaseFactCheck[Showcase_fact_check_Grok]
  end

  Article --> LogDir
  Prompts --> LogDir
  Research --> LogDir
  FactCheck --> LogDir

  LogDir --> ShowcaseRoot
  ShowcaseRoot --> ShowcaseFolder
  ShowcaseFolder --> ShowcaseReport
  ShowcaseFolder --> ShowcaseFactCheck
```
