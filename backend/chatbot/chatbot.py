import os
from openai import AzureOpenAI
from websocket_server import WebsocketServer
import io from 'socket.io-client';

    class Chat extends React.Component {
     constructor(props) {
       super(props);
       this.state = {
         messages: [],
         socket: null
       };
    }

    componentDidMount() {
        const socket = io('http://localhost:12345');
        socket.on('message', message => {
        this.setState(prevState => ({
           messages: [...prevState.messages, message]
        }));
       });
       this.setState({ socket });
     }

     sendMessage = (message) => {
       this.state.socket.emit('message', message);
       this.setState(prevState => ({
         messages: [...prevState.messages, { text: message, sender: 'user' }]
       }));
     };

     // ... phần còn lại của component ...
   }

   export default Chat;
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2023-05-15"
)

def get_bot_response(message):
    response = client.chat.completions.create(
        model="GPT35TURBO16K",
        messages=[
            {"role": "system", "content": "Bạn là 1 giáo viên, và bạn trả lời bằng tiếng Việt"},
            {"role": "user", "content": message},
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

ef new_client(client, server):
    print(f"New client connected with id {client['id']}")

def message_received(client, server, message):
    response = get_bot_response(message)
    server.send_message(client, response)

server = WebsocketServer(port=12345, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()

