<template>

  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}


body {
  font-family: 'Source Sans Pro', 'Trebuchet MS', 'Lucida Grande', 'Bitstream Vera Sans', 'Helvetica Neue', sans-serif;
  margin: 0;
  text-align: center;
  color: #293c4b;
}


img {
  margin: 20px 0;
  max-width: 200px;
}


.subText {
  color: cornflowerblue;
  padding-top: 50px;
  font-size: 0.8em;
  font-style: italic;
}

.mainText {
  color: darkcyan;
  padding-top: 50px;
  padding-bottom: 50px;
  font-size: 2.5em;
}

.header {
  color: brown;
  /* padding-top: 0.5em; */
  /* padding-bottom: 1em; */
  font-size: 3em;
}

.pad-right {
  padding-right: 50px;
}
</style>
