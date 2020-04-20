<template>
  <div class="hello">
    <div class="jumbotron jumbotron-fluid">
      <h1>{{ msg }}</h1>
      <p>
        Click the large "Generate" butteon, to generate some animal names
      </p>
      <div class="clicketido">
        <b-button class="buttons" variant="success" v-on:click="generateName()">Generate&nbsp;<b-icon icon="arrow-repeat"></b-icon></b-button>
        <b-button variant="danger" v-on:click="clear()">Clear&nbsp;<b-icon icon="trash"></b-icon></b-button>
      </div>
    </div>

    <div class="results" v-if="data">
      First: {{ data.first | capitalize }}
      Second: {{ data.second | capitalize }}
      TimeStamp: {{ data.timestamp }}

    </div>

    <div class="error" v-if="error">
      Something failed!!!
    </div>


  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      data: null,
      error: null
  }
},
methods : {
  generateName(){
    fetch("http://localhost:5000/")
      .then(stream => stream.json())
      .then(data => {
        this.data = {
          first: data.first,
          second: data.second,
          timestamp: data.timestamp
        }
        this.error = null
      })
      .catch(error => {
        console.error(error)
        this.error = error
      })
  },
  clear(){
    this.data = null
    this.error = null
  }
}
// mounted(){
//     fetch("http://localhost:5000/")
//     .then(stream => stream.json()).then(data => this.data = data).catch(error => console.error(error))
//   }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.buttons {
  margin-right: 2em;
}

.buttons b-icon {
  padding-left: 5em;
}
</style>
