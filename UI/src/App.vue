<template>
  <div id="app">
      <Header />
      <div id="app-container" class="no-sidebar">
        <!-- <div id="sidebar">
        <div class="logo align-center">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Logo_Google_2013_Official.svg" alt="Google"/>
        </div>
        <div class="separator">

        </div>
        <div class="menu">
            <ul>
                <li><router-link  active-class="active" to="/search" exact>Search</router-link></li>
                <li><router-link  active-class="active" to="/" exact>Dashboard</router-link></li>
            </ul>
        </div>
        </div> -->
        <div id="body-container">
            <router-view></router-view>
        </div>
        </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VueRouter from 'vue-router';
import Header from './components/Header.vue';
import Dashboard from './components/Dashboard.vue';
import SinglePerson from './components/SinglePerson.vue';
Vue.use(VueRouter);
const router = new VueRouter({
  routes: [
    { path: '/', component: Dashboard },
    { path: '/person/:id', component: SinglePerson, props: true },
    { path: '/search', component: Dashboard },
  ]
});
export default {
  name: 'app',
  components: { Header
  },
  data() { 
    return {
      tableHeadings: ['id', 'name', 'dob', 'Name Match', 'DOB Match'],
      persons: [
          {
              id: 123723,
              name: 'Renuka Poluru',
              dob: '13/08/1994',
              nameMatch: 80,
              dobMatch: 100
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          },
          {
              id: 123724,
              name: 'Subham',
              dob: '21/05/1994',
              nameMatch: 30,
              dobMatch: 100
          },
          {
              id: 123725,
              name: 'Test 3',
              dob: '11/02/1990',
              nameMatch: 60,
              dobMatch: 100
          },
          {
              id: 123726,
              name: 'Test 4',
              dob: '13/08/1994',
              nameMatch: 20,
              dobMatch: 20
          }
      ],
      searchString: ''
    }
  },
  filters: {
      getColor(percentage) {
          if(percentage == undefined || null) {
              return 'red'
          } else if(percentage >= 70) {
              return 'green'
          } else if(percentage >= 50) {
              return 'yellow'
          } else {
              return 'red'
          }
      },
  },
  computed: {
      filteredPersons(){
          if(this.searchString){
              return this.persons.filter((item)=>{
                  return item.name.toLowerCase().includes(this.searchString.toLowerCase());
              })
          } else{
              return this.persons;
          }
      }
  },
  router
}

</script>

<style>
    body {
        width:100%;
        margin:0;
        font-family: 'Roboto Condensed', sans-serif;
        font-size: 16px; 
        color:#2B3131;                                                               
    }

    * {
        box-sizing: border-box;
    }

    img {
        max-width:100%;
    }

    h1, h2, h3, h4, h5, h6, p {
        margin: 0 0 30px;
    }

    .align-center {
        text-align: center;
    }

    #app-container {
        display:flex;
        display:-webkit-flex;
        display:-ms-flex;
        align-items: stretch;
    }
    #sidebar {
        background:#2B3131;
        padding:20px 0px;
        width:300px;
        min-height: 100vh;
        color:#fff;
    }

    #sidebar .menu ul {
        margin:0;
        padding:0;
        list-style: none;;
    }

    #sidebar .menu a {
        text-decoration: none;
        color:#fff;
        padding:15px 20px;
        position:relative;
        transition:all ease-in-out .3s;
        display:block;
        width:100%;
    }

    #sidebar .menu a:before {
        position:absolute;
        content:'';
        width:5px;
        height:100%;
        background:#79D5D4;
        opacity:0;
        transition: all ease-in-out .3s;
        top:0;
        left:0;
    }

    #sidebar .menu a.active:before {
        opacity: 1;
    }

    #sidebar .menu a.active {
        background:#fff;
        color:#2B3131;
    }

    #sidebar .logo {
        padding:10px 20px;
    }

    #sidebar .separator {
        height: 40px;
        background: #384242;
    }

    .logo img {
        max-height:40px;
    }

    #body-container {
        width:calc(100% - 300px);
        background:#EFF7F9;
        padding:50px 30px;
    }

    .no-sidebar #body-container {
        width: 100%;
        min-height: 100vh;
    }

    #data-table,
    table#person-table {
        width: 100%;
        text-align: left;
        box-shadow: 0 0 7px 1px #0000003b;
        border-spacing: 0;
        background:#fff;
    }

    #data-table tr th, #data-table tr td,
    #person-table tr td {
        padding: 15px;
        border-spacing: 0;
        border-collapse: collapse;
        font-size: 14px;
        font-weight: 500;
    }

    #data-table tr td.remarks {
      font-size: 12px;
      width: 20%;
    }

    #data-table tr td a {
        color:#2B3131;
    }
    
    #data-table tbody tr:nth-child(2n+1) td,
    #data-table tr:nth-child(2n+1) td,
    #person-table tr:nth-child(2n) td{
        background:#F8F8F8;
    }

    #data-table tr th,
    #person-table tr th {
        background:#79CED3;
        color:#fff;
    }

    #person-table tr td:first-child {
      font-weight: bold;
    }

    #data-table tr td.green,
    #person-table tr td.green,
    #data-table tr td.green a {
        color:#1ee21e;
    }

    #data-table tr td.yellow,
    #person-table tr td.yellow,
    #data-table tr td.yellow a {
        color:gold;
    }

    #data-table tr td.red,
    #person-table tr td.red,
    #data-table tr td.red a {
        color:red;
    }

    input, select {
        width: 100%;
        max-width: 300px;
        padding: 10px 10px;
        font-family: 'Roboto Condensed', sans-serif;
        font-size: 16px;
        margin-bottom: 30px;
        margin-right:20px;
        -webkit-appearance: none;
        -moz-appearance: none;
        -ms-appearance: none;
        appearance: none;
        border:0;
        border:1px solid #e1e1e1;
    }

    select {
      background:#fff url('./assets/caret-down.png');
      background-position: center right;
      background-repeat: no-repeat;
      background-position-x: 95%;
      background-size: 12px;
    }

    #data-table tr td.remarks ul {
        padding: 0;
        margin: 0;
        list-style: none;
    }

    #data-table tr td span {display: block;width: 100%;}

    #data-table tr td span:first-child {
        margin-bottom: 10px;
    }
</style>
