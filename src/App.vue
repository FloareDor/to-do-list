<template>
  <div class="container">
    <div class="lists-container">
      <div class="todo-list">
        <div class="title"></div>
        <div>
          <h2>To Do List</h2>
          <div v-for="(todo, index) in todos" :key="index">
            <div class="input-container">
              <input v-model="todo.text" placeholder="" @click="generateRandomColor(todo), playNote()" class="input-style" :style="{ backgroundColor: todo.bgColor }" @keydown.enter="moveToDone(index)"/>
              <button @click="moveToDone(index)" class="move-to-done">Done</button>
            </div>
          </div>
          <button @click="addTodo()">+</button>
        </div>
      </div>
      <div class="done-list">
        <h2>Done List</h2>
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
export default {
  data() {
    return {
      todos: [{ text: '', bgColor: '#FB9999' }],
      dones: [],
    }
  },
  methods: {
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
    generateRandomColor(todo) {
      const randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
      todo.bgColor = randomColor;
    },
    addTodo() {
      this.todos.push({ text: '', bgColor: '#FB9999' });
    },
    moveToDone(index) {
      this.playChord()
      const todo = this.todos[index];
      if (todo.text !== '') {
        this.dones.push({ text: todo.text, bgColor: todo.bgColor });
        // this.done.bgColor=todo.bgColor;
        

        if(index!=0){
          this.todos.splice(index, 1);
        }
        else{
          todo.text='';
        }
      }
    },
  },
}
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.lists-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
}

.todo-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: calc(50% - 30px);
  max-width: 500px;
  border-radius: 25px;
  
}

.done-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: calc(50% - 30px);
  max-width: 500px;
  border-radius: 25px;
}

.done-input {
  position: relative;
  width: 100%;
  max-width: 500px;
  height: 38.5px;
  margin: 10px auto;
  padding: 0 20px;
  border-radius: 25px;
  align-self: center;
  outline: none;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
  border: none;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

@media screen and (max-width: 768px) {
  .lists-container {
    flex-direction: column;
    align-items: center;
  }
  
  .todo-list,
  .done-list {
    width: 100%;
    margin-bottom: 20px;
  }
}
</style>
