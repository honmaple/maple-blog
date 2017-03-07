import Org from 'org'
import marked from 'marked'
import hljs from 'highlight.js'


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
  // marked.setOptions({
  //   highlight: function (code) {
  //     return hljs.highlightAuto(code).value;
  //   }
  // });
  return marked(text);
}
// function markdown (text) {
//   converter = new showdown.Converter();
//   return converter.makeHtml(text);
// }
function markup(type,text) {
  if (type == '1'){
    return orgmode(text);
  }else {
    return markdown(text);
  }
}
export default markup
