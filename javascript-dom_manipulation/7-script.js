getData();

async function getData() {
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
  const data = await response.json();
  const arr = data.results;
  for (let i = 0; i < arr.length; i++) {
    var x = document.createElement('li');
    x.textContent = arr[i].title;
    list = document.getElementById('list_movies');
    list.appendChild(x);
  }
}