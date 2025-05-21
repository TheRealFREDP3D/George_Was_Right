# George-Was-Right v0.6 - README.md

![Generated with DALL-E and a prompt from the Prompt Master Agent](images/Header.png)

George_Was_Right leverages a team of AI agents, powered by CrewAI, to analyze recent world events through the lens of themes from George Orwell's *1984*. It orchestrates four specialized agents—Researcher, Writer, Prompt Master, and Editor—to perform tasks such as:

- **ResearcherAgent**: 
    - Role: "Expert Researcher in Political and Societal Developments"
    - Goal: "Investigate significant global political or societal developments that reflect similarities or parallels found within Orwell's '1984', focusing on surveillance practices or control over information narratives by governing bodies or powerful entities."
- **WriterAgent**:
    - Role: "Comparative Analyst and Writer"
    - Goal: "Synthesize researched occurrences into comprehensive comparative analyses between modern-day developments and thematic elements from Orwell's '1984', highlighting why contemporary incidents mirror '1984' scenarios."
- **PromptMasterAgent**:
    - Role: "Visual Concept Creator for Socio-Political Commentary"
    - Goal: "Generate visually compelling representations (infographics or artwork) based on the comparative analyses from the Researcher and Writer Agents, visually communicating connections between '1984' themes and modern occurrences."
- **EditorAgent**:
    - Role: "Guardian of Clarity and Thematic Cohesion"
    - Goal: "Ensure all generated content (analyses, articles, and visual prompt descriptions) is clear, grammatically impeccable, thematically coherent with Orwellian concepts, and maintains a consistent tone and high quality suitable for publication."

This project aims to provide a nuanced examination of how contemporary society reflects Orwellian concerns about digital privacy and freedom, fostering meaningful discussion and awareness.

---

![Generated with DALL-E and a prompt from the Illustrator Agent](images/illustration-under-surveillance-camera.jpg)

---

## Features and Roadmap

### Current Features

- **Automated Research and Analysis:** Gathers and analyzes news stories in relation to *1984* themes.
- **Multi-Agent Collaboration:** Uses specialized AI agents (Researcher, Writer, Prompt Master, Editor) to divide and conquer complex tasks.
- **Visual Prompt Generation:** Produces creative prompts for illustrations to enhance storytelling and audience engagement.
- **Clear and Structured Output:** Outputs organized markdown reports combining research, analysis, and visuals.
- **Environment Variable Validation:** Validates required environment variables and provides error handling.
- **Improved Code Structure:** Enhanced code organization and readability.
- **LLM Model Support:** Integrates various LLM models for enhanced functionality.

### Upcoming Enhancements

- **Customizable Search Parameters:** Add options for users to specify country and the number of search results for focused research.
- **GUI Integration:** Develop a user-friendly graphical interface for seamless control of the analysis process.
- **Refined Output Formats:** Improve markdown and PDF exports for clarity and usability.
- **Incremental Feature Rollout:** Continuously implement new features while maintaining backward compatibility.

![Generated with DALL-E and a prompt from the Illustrator Agent](images/Header.png)

## Showcase

### Showcase-1

- **Main Script:** [main.py](showcase/Showcase-1/main.py)
- **Generated Images:**
  - [Prompt1-ChatGPT.jpg](showcase/Showcase-1/Prompt1-ChatGPT.jpg)
  - [Prompt1.Dall-E-2.jpg](showcase/Showcase-1/Prompt1.Dall-E-2.jpg)
  - [Prompt1.Dall-E-3.jpg](showcase/Showcase-1/Prompt1.Dall-E-3.jpg)
  - [Prompt1.Dall-E-4.jpg](showcase/Showcase-1/Prompt1.Dall-E-4.jpg)
  - [Prompt1.Dall-E.jpg](showcase/Showcase-1/Prompt1.Dall-E.jpg)
  **Terminal Log:** [terminal_log.md](showcase/Showcase-1/terminal_log.md)

### Showcase-2

- **Generated Images:**
  - [Prompt1-ChatGPT.jpg](showcase/Showcase-2/Prompt1-ChatGPT.jpg)
  - [Prompt2-Dalle-E-2.jfif](showcase/Showcase-2/Prompt2-Dalle-E-2.jfif)
  - [Prompt2-Dalle-E-3.jfif](showcase/Showcase-2/Prompt2-Dalle-E-3.jfif)
  - [Prompt2-Dalle-E-4.jfif](showcase/Showcase-2/Prompt2-Dalle-E-4.jfif)
  - [Prompt2-Dalle-E.jfif](showcase/Showcase-2/Prompt2-Dalle-E.jfif)
- **Terminal Output:** [terminal-output--26-12-2024.md](showcase/Showcase-2/terminal_log2.md)

---

![Generated with DALL-E and a prompt from the Illustrator Agent](images/the-eye-telescreen.jpg)

---

## Project History

George-Was-Right is a project I’ve been working on to learn Python. I needed  way to get hands-on with programming and not just read about it.

Like a lot of people during the pandemic, I was stuck at home with too much time on my hands. That’s when I decided to finally dive back into coding. I had just finished reading '1984' and taught, “Why not make something in George Orwell’s world?” My first idea was to make a small game. I wasn't really serious about this project until I discovered LLMs, Ollama and CrewAI. My project idea took a hard left turn. It was definitely a stretch for my skills at the time, but I love a good challenge. It forced me to read, learn, and experiment. Plus, who doesn’t like an excuse to Google stuff?

What started as a “just for fun” hobby has turned into something more. I’m working on it in my spare time because, as much as I find it’s fun and satisfying, it doesn't pay the bills.

---

This consist of the second iteration of George-was-Right. The original version became unmanageable due to accumulating changes and a lack of version control. Starting fresh enabled a focus on better coding practices, structured development, and Git-based version control.

I hope you find this project interesting.

---

### Lessons Learned the Hard Way

- Importance of planning and incremental development.
- Effective use of Git for managing changes.
- Best practices for Python project structuring and imports.
- Benefits of regular backups and separating development from production environments.
- Keeping notes and documentation updated.

---

![Generated with DALL-E and a prompt from the Illustrator Agent](images/ministry-of-truth-soviet-touch.jpg)

---

## Getting Started

Follow these steps to set up the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/TheRealFREDP3D/George_Was_Right.git
   ```

2. Navigate to the project directory:

   ```bash
   cd George_Was_Right
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Get an API key for free from Github and add it to your .env file.
   - Go to the Marketplace and search for "Github API" and click on the "Get it free" button.
   - Add the API key to your .env file.

   ```bash
   GITHUB_API_KEY=your_github_api_key
   ```

7. Get an API key for free from SerperDev and add it to your .env file.

   ```bash
   SERPER_API_KEY=your_serper_api_key
   ```

8. Run the project:

   ```bash
   python main.py
   ```

The project will run and create logs in the /log folder.

---

**Requirements:**

- Python 3.8 or later
- Internet connection for AI-powered agents or use Ollama for local usage.
- Github API key
- SerperDev API key

## Notes

It's possible to use other LLM models, but you will need to change the model in the .env file and tweak the code in the src/llm.py file. By default I used gpt-4o because it produces the best results without having to pay for it. I have made a lot of tests with other models and I can say that the results are not always good.

Please, be aware that the LLM models have different capabilities and limitations.

Feel free to use the code as you see fit. I'm not a professional programmer, so I'm sure there are many improvements that can be made...

If you have any questions or suggestions, please feel free to contact me or open an issue.
And I'm curious and really interested to know what you think about this project and if you have any ideas for improvements.

I would appreciate learning about which models you've tried and what works best for you to add a listing to the documentation.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your message here"
   ```

4. Push the branch to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Submit a pull request.

Please ensure changes are well-tested and documented. Refer to the [Contribution Guide](CONTRIBUTING.md) for more details.

---

## Contact

| **Contact**        | **Links**                                                             |
|--------------------|-----------------------------------------------------------------------|
| Twitter            | [@TheRealFredP3D](https://twitter.com/TheRealFredP3D)                 |
| GitHub             | [@TheRealFREDP3D](https://github.com/TheRealFREDP3D)                  |
| Email              | [fredp3d@proton.me](mailto:fredp3d@proton.me)                         |
| Link Gallery       | [LinkGallery](http://link.gallery/therealfredp3d)                     |

---

**License:** MIT License. See the [LICENSE](LICENSE) file for details.

---

![Generated with DALL-E and a prompt from the Illustrator Agent](images/big-brother-is-watching.jpg)

**Modified:** April 27, 2025
