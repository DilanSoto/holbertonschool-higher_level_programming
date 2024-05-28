const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function() {
    const newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    const myList = document.querySelector('.my_list');
    myList.appendChild(newListItem);
});
