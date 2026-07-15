document.getElementById('add_item').onclick = addItem;

function addItem() {
  x = document.createElement('li');
  t = document.createTextNode('Item');
  x.appendChild(t);
  ul = document.querySelector('ul');
  if (ul.classList.contains('my_list')) {
    ul.appendChild(x);
  }
}