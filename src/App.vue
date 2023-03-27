<template>

  <div class="container">
    <div class="lists-container">
      <div class="todo-list">
        <div class="title"></div>
        <button @click="clear()" class="clear">Clear</button>
        
        <div>
          <h2>To Do List</h2>
          <div v-for="(todo, index) in todoList" :key="index">
            <div class="input-container">
              <input v-model="todo.text" placeholder="Your Todo Note" 
                @click="generateRandomColor(todo), playNote()"
                class="input-style" 
                :style="{ backgroundColor: todo.bgColor }"
                @keydown.enter="addTodo(todo.text, 1, index)"
                onload="setup()"/>
              <button @click="moveToDone(index)" class="move-to-done">Done</button>
            </div>
          </div>
          <button @click="addTodo('', 0)"  class="plus">+</button>
        </div>
      </div>
      <div class="done-list">
        <h2>Done</h2>
        <div v-for="(done, index) in dones" :key="index" >
          <div class="input-container">
            <input v-model="done.text" class="done-input" readonly/>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>


import Axios from "axios";
import { onMounted } from "vue";
//const toDoUrl = "http://127.0.0.1:5000/"


export default {
  data() {
    return {
      todoList: [{ text: '', bgColor: '#FB9999' }],
      todoItem: {},
      dones: [],
      editMode: false,
    }
  },
  
  methods: 
  {
    

    saveDoneItem(doneItem, index){
      const requestBody = { "done": doneItem, "index": index};
      Axios.post('http://192.168.29.45:5000/api/adddone', requestBody)
      .then(response => {
      console.log('New done item was successfully sent to server:', response.data);
      })
      .catch(error => {
      console.error('Failed to send new done item to server:', error);
      });
    },

    saveTodoItem(todoItem){
      const requestBody = { "todo": todoItem };
      Axios.post('http://192.168.29.45:5000/api/addtodo', requestBody)
      .then(response => {
      console.log('New To Do item was successfully sent to server:', response.data);
      })
      .catch(error => {
      console.error('Failed to send new To Do item to server:', error);
      });
    },

    addTodo(input, bool, index, color){
      if(bool==1 && index!=0){
        return 0
      }
      const newTodo = { text: input, bgColor: '#FB9999' };
      this.todoList.push(newTodo);
      if(bool!=1){
        console.log("normal");
      }
      else{
        const todo = this.todoList[index];
        todo.text='';
      }
      if(bool!=2){
        this.saveTodoItem(input);
      }
    },
    generateRandomColor(todo) {
      const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
      todo.bgColor = randomColor;
    },
    moveToDone(index) {
      this.playChord()
      const todo = this.todoList[index];
      if (todo.text !== '') {
        this.dones.push({ text: todo.text, bgColor: todo.bgColor });
        this.saveDoneItem(todo.text, index); // send to api
        // this.done.bgColor=todo.bgColor;
        if(index!=0){
          this.todoList.splice(index, 1);
        }
        else{
          todo.text='';
        }
      }
      
    },
    playNote(){
      const notes = ["c", "d", "e", "f", "g", "a", "b", "c5"];
      const index = Math.floor(Math.random() * notes.length);
      const randomNoteAddr = 'public/sounds/'+notes[index] + ".mp3";
      console.log(randomNoteAddr);
      var note = new Audio(randomNoteAddr);
      note.play();
    },
    playChord(){
      const chords = ["1", "2", "3", "4", "5"];
      const index = Math.floor(Math.random() * chords.length);
      const randomChordAddr = 'public/sounds/chord'+chords[index] + ".mp3";
      console.log(randomChordAddr);
      var chord = new Audio(randomChordAddr);
      chord.play();
    },
    setup() {
      console.log("MOUNTED");
      Axios.get('http://192.168.29.45:5000/api/getdata')
      .then(response => {

        // Adding all todos
        var json_data = response.data;
        var n_of_todos = Object.keys(json_data["todo"]).length
        console.log(n_of_todos);
        console.log(json_data);
        if (n_of_todos>0){
          for( let i=0; i<n_of_todos; i++){
            console.log(json_data["todo"][i]);
            this.addTodo(json_data["todo"][i], 2);
          }
        }
        // Adding all dones
        var n_of_dones = Object.keys(json_data["done"]).length
        console.log(n_of_dones);
        console.log(json_data);
        if (n_of_dones>0){
          for( let i=0; i<n_of_dones; i++){
            console.log(json_data["done"][i]);
            this.dones.push({ text: json_data["done"][i] });
          }
        }
      })
      .catch(error => {
        console.log(error);
      });

    },
    clear(){
      Axios.post('http://192.168.29.45:5000/api/clear');
      this.todoList=[{ text: '', bgColor: '#FB9999' }];
      
      this.dones = [];
      this.playChord();
    },
    logtheshitoutofit(){
      console.log(this.todoList);
    }
  },

  mounted: function() {
    this.setup();
    console.log("Mounted!");
  },
      
};
</script>


<style>

.nav{
  /* Login */
outline: none;
box-sizing: 0;
position: fixed;
font-size: 1.5vw;
font-weight: bold;
margin-bottom: 20px;
color: #D9D9D9;
font-family: 'JetBrains Mono', monospace;
font-style: normal;
top:2%;
right:1.5%;
margin-bottom: 20px;
text-underline-offset:0;
}

</style>