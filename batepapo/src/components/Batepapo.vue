<template>
  <div v-if="visivel" class="card">
    <div class="card-body">
      <span
        v-bind:title="conversa.timestamp"
        v-for="conversa in conversas"
        :key="conversa.timestamp"
        ><b>{{ conversa.nome | confere_nick | exemplo("Nome") }}</b> disse:
        {{ conversa.msg | chatguard }}<br
      /></span>
    </div>
    <div class="card-footer">
      <div class="form-group mb-3">
        <input
          v-model="digitado"
          class="form-control"
          type="text"
          name=""
          id=""
        />
        <div class="input-group-append">
          <button class="btn btn-primary" @click="send" type="button">
            Enviar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios").default;
export default {
  name: "Batepapo",
  props: ["username", "visivel", 'chat'],
  data: function () {
    return {
      conversas: [],
      digitado: "",
    };
  },
  filters: {
    confere_nick: function (nick) {
      let bloquear = ["bobo", "cara de mamão", "feio"];
      if (bloquear.indexOf(nick) == -1) {
        // pode
        return nick;
      } else {
        return "nick inválido";
      }
    },
    chatguard: function (mensagem) {
      let bloqueadas = ["água"];
      for (let palavra of bloqueadas) {
        mensagem = mensagem.replace(palavra, "******");
      }
      return mensagem;
    },
    exemplo: function (a, b) {
      return b + " : " + a;
    },
  },
  methods: {
    send: function () {
      let nome = "anônimo";
      if (this.username != undefined) nome = this.username;
      console.log(`${nome} : ${this.digitado}`)
    
      axios
        .post("http://127.0.0.1:5000/chat", {
          chat: this.chat,
          nome: nome,
          msg: this.digitado,
          timestamp: new Date().toLocaleTimeString(),
        })
        .then(function (response) {
            console.log(response)
            console.log(response.data)
          return response.data
        })
        .catch(function (error) {
          console.log(error);
        }).then(result => this.conversas = result);
    },
  },
};
</script>

<style>
</style>