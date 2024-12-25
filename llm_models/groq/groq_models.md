Production Models
MODEL ID	DEVELOPER	CONTEXT WINDOW (TOKENS)	MAX OUTPUT TOKENS	MAX FILE SIZE	MODEL CARD LINK
distil-whisper-large-v3-en	HuggingFace	-	-	25 MB	
Card
gemma2-9b-it	Google	8,
192	-	-	
Card
gemma-7b-it (DEPRECATED)	Google	8,
192	-	-	
Card
llama-3.3-70b-versatile	Meta	128k	32,
768	-	
Card
llama-3.1-70b-versatile (DEPRECATED)	Meta	128k	32,
768	-	
Card
llama-3.1-8b-instant	Meta	128k	8,
192	-	
Card
llama-guard-3-8b	Meta	8,
192	-	-	
Card
llama3-70b-8192	Meta	8,
192	-	-	
Card
llama3-8b-8192	Meta	8,
192	-	-	
Card
mixtral-8x7b-32768	Mistral	32,
768	-	-	
Card
whisper-large-v3	OpenAI	-	-	25 MB	
Card
whisper-large-v3-turbo	OpenAI	-	-	25 MB	
Card

Preview Models
Note: Preview models are intended for evaluation purposes only and should not be used in production environments as they may be discontinued at short notice.

| MODEL ID                              | DEVELOPER | CONTEXT WINDOW (TOKENS) | MAX OUTPUT TOKENS | MAX FILE SIZE | MODEL CARD LINK |
|---------------------------------------|-----------|-------------------------|-------------------|---------------|-----------------|
| llama3-groq-70b-8192-tool-use-preview | Groq      | 8,192                   | -                 | -             | Card            |
| llama3-groq-8b-8192-tool-use-preview  | Groq      | 8,192                   | -                 | -             | Card            |
| llama-3.3-70b-specdec                 | Meta      | 8,192                   | -                 | -             | Card            |
| llama-3.1-70b-specdec                 | Meta      | -                       | 8,192             | -             | Card            |
| llama-3.2-1b-preview                  | Meta      | 128k                    | 8,192             | -             | Card            |
| llama-3.2-3b-preview                  | Meta      | 128k                    | 8,192             | -             | Card            |
| llama-3.2-11b-vision-preview          | Meta      | 128k                    | 8,192             | -             | Card            |
| llama-3.2-90b-vision-preview          | Meta      | 128k                    | 8,192             | -             | Card            |

See our deprecated models here 


Hosted models are directly accessible through the GroqCloud Models API endpoint using the model IDs mentioned above. You can use the https: //api.groq.com/openai/v1/models endpoint to return a JSON list of all active models: