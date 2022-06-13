affection_level = document.querySelector('#affection_level')

const form = document.querySelector('#form_cat')
const select = document.querySelector('#breed')

select.addEventListener('change', (e) => {form.submit()})

for(i=0; i< affection_level_paws; i++){
  affection_level.innerHTML += '<span class="fa-lg fa fa-paw mx-auto"></span><span> </span>'
}

select.value = breed
select.text = breed