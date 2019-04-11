import './main.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { Elm } from './Main.elm';
import registerServiceWorker from './registerServiceWorker';

Elm.Main.init({
  node: document.getElementById('root')
});

registerServiceWorker();
