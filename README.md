# SETUP
Clone the repo.
```bash
git clone [https://github.com/yourusername/RenovAgent.git](https://github.com/Sharan2001/RenovAgent.git)
cd RenovAgent
```

## Create a virtual environment.
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## Install the dependencies.
```bash
pip install -r req.txt
```

## Add the OpenAI API key to .env file.
```bash
OpenAI="yourKey"
```
API Key is - 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

## Running the APP 
## Start the server 
```bash
uvicorn main:app --reload
```
### Open browser at: http://127.0.0.1:8000  

![Project Structure](screenshot.png)

## UI: 
  • Has the active agent name.\
  • A record button for speaking.\
  • Current conversation between user and agent.\
  • Add this line after line 79 in conversation.py for history logs.
  ```python
  Type: {self.history}
```  

## Usage/Demo: 
   • Press and hold the record button to speak.\
   • Wait for a few seconds for response.\
   • Bob/Alice voices will be reflected in the TTS output.\
   • Bob and Alice have different voice and switching between agents takes some time for them the get the context.

## Example phrases: 
   • “Hi Bob, I want to remodel my kitchen with a $25k budget.”\
   • “Transfer me to Alice.”\
   • “Go back to Bob.”

## Reflection: 
   • Currently the streaming function for SST and TTS is not active. Due to this there is evident delay in the response. However with more time, I can impliment this over websocket and chunking of audio transcripts with time delay for end of conversation to achieve near real time feedback. The trade off for that is cost of using the encoder decoder locally to have lowe latency from speech to text and text to speech. Live translation would be faster.\
   • Agents switch correctly but there is room for improvement for seamless transfer. I can use structured handoff rules and use embeddings for faster context understanding. Right now once they switch the new agent will not respond immediately and have to be asked anothter question and will answer everything together. I ca improve that drastically with more time.\
   • Maintaining context over multi-turn or multi-step dialogues is a challenge. With time I can use context and histry window to effectively make the agents understand better.\
   • Right now the agents do not have interruption ability. I am trying to figure out how to implement voice activity detection and make the agents stop generating and listen to new inputs.\
   • UI/UX is basic with no design. Can be inproved in the future.

## Future Improvements: 
   • Streaming SST and TTS: Send chunks of spoken words to convert to text and play audio as LLM generates it.\
   • Local LLM integration: Run responses offline.\
   • Contextual memory: Save conversation state across sessions.\
   • Better partial transcript accuracy: Use smaller chunk size for faster updates.\
   • Incorporate interruption for the agents.\
   • Better UI/UX.
  
