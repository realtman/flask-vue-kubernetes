<template>
    <div class="header-body">
        Rest Api Demo
        <hr/>
        <p>Sample Rest API without authentication</p>
        <button v-on:click="showExample1 = !showExample1"> Show/ Hide</button>
        <p v-if="showExample1">Sample Rest API w/ Authentication:<pre>{{info}}</pre></p>
        <hr/>
        <p>Your OAuth ID Token</p>
        <textarea v-model="idToken" cols="128" rows="10"></textarea>
        <br>
        <button v-on:click="getGenomes">Click Me To Get Genomes</button>
        <p>{{genomes}}</p>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "RestApiExampleView",
        data() {
            return {
                info: '',
                showExample1: false,
                genomes:'',
                idToken: "",

            }
        },
        created() {
            axios
            .get('https://api.coindesk.com/v1/bpi/currentprice.json')
            .then(response => (this.info = response))
        },
        mounted: function () {
            // Overkill for setting a variable, but an example of how
            //  to tie into a component's lifecycle
            this.$nextTick(function () {
                // Code that will run only after the
                // entire view has been rendered
                this.idToken = this.$cookies.get('idToken');
            })
        },
        methods: {
            getGenomes() {
                // eslint-disable-next-line
                console.log("Getting genomes");
                axios
                    .get('https://genome-service.cibo-inari.com/v1/refgenome',
                        {
                            headers: {
                                Authorization: 'Bearer ' + this.idToken
                            }
                        }
                    )
                    .then(response => (this.genomes=response))
                    .catch(error => {
                        if (error.response) {
                            // The request was made and the server responded with a status code
                            // that falls out of the range of 2xx
                            // eslint-disable-next-line
                            console.log(`Code: ${error.response.status} Response: ${error.response.data} Headers: ${error.res}`);
                            // eslint-disable-next-line
                            console.log(error.response.headers);
                        } else if (error.request) {
                            // The request was made but no response was received
                            // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                            // http.ClientRequest in node.js
                            // eslint-disable-next-line
                            console.log(`No Response received` ,error.request);
                        } else {
                            // Something happened in setting up the request that triggered an Error
                            // eslint-disable-next-line
                            console.log('Request Error', error.message);
                        }
                        // console.log(error.config);
                    })

            }
        }
    }
</script>