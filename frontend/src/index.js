import './main.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { Elm } from './Main.elm';
import registerServiceWorker from './registerServiceWorker';


//console.log(process.env.API_URL);

if ( process.env.API_URL ){
  console.log("Got API_URL")
  console.log(process.env.API_URL)
  console.log("Using this in the app")
  Elm.Main.init({
    node: document.getElementById('root'),
    flags: {
      url: process.env.API_URL
    } 
  });
} else {
  console.log("Using localhost for backend")
  console.log("Using http://localhost:5000/json")
  Elm.Main.init({
    node: document.getElementById('root'),
    flags: {
      url: "http://localhost:5000/json"
    }
  });
}



registerServiceWorker();
