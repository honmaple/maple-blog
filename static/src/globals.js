import Org from 'org'
import marked from 'marked'
// import { showdown } from 'showdown'


function orgmode (text) {
  var parser = new Org.Parser();
  var orgDocument = parser.parse(text);
  var orgHTMLDocument = orgDocument.convert(Org.ConverterHTML, {
    headerOffset: 3,
    exportFromLineNumber: false,
    suppressSubScriptHandling: false,
    suppressAutoLink: false
  });
  return orgHTMLDocument.toString();
}

function markdown (text) {
  return marked(text);
}
// function markdown (text) {
//   converter = new showdown.Converter();
//   return converter.makeHtml(text);
// }

export default {orgmode,markdown}
