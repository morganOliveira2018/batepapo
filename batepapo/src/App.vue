<template>
  <!-- Observe que aqui apenas trouxe o template do modelo anterior pro local correto -->
  <div id="app" class="container-fluid">
    <div class="jumbotron">
      <h1>DW Chat</h1>
      <p>O seu chat para discutir qualquer coisa.</p>
    </div>
    <div class="row">
      <!-- canais -->
      <div class="col-2">
        <meusCanais
          v-on:mudacanal="mudaCanal"
          v-bind:canais="canais"
        ></meusCanais>
      </div>
      <!-- bate papo -->
      <div class="col-8">
        <batepapo
          chat="bccdw"
          v-bind:visivel="mostra1"
          v-bind:username="nome_usuario"
        ></batepapo>
        <batepapo
          chat="animes"
          v-bind:visivel="mostra2"
          v-bind:username="nome_usuario"
        ></batepapo>
        <batepapo
          chat="viagens"
          v-bind:visivel="mostra3"
          v-bind:username="nome_usuario"
        ></batepapo>
      </div>
      <!-- stickers -->
      <div class="col-2">
        <input
          v-model="nome_usuario"
          class="form-control"
          type="text"
          name=""
          id=""
          placeholder="escolha seu nick"
        /><br />

        sticker 1<br />
        sticker 2<br />
        sticker 3<br />
      </div>
    </div>
  </div>
</template>

<script>
import Batepapo from "./components/Batepapo";
import MeusCanais from "./components/Meuscanais";
export default {
  name: "App",
  components: {
    Batepapo,
    MeusCanais,
  },
  data: function () {
    return {
      nome_usuario: "anônimo",
      canais: [
        { id: "1", titulo: "BCC-DW" },
        { id: "2", titulo: "Animes" },
        { id: "3", titulo: "Viagens" },
      ],
      mostra1: true,
      mostra2: false,
      mostra3: false,
    };
  },
  methods: {
    mudaCanal: function (id) {
      console.log(`O canal de id ${id}`);
      if (id == "1") {
        this.mostra1 = true;
        this.mostra2 = false;
        this.mostra3 = false;
      } else if (id == "2") {
        this.mostra1 = false;
        this.mostra2 = true;
        this.mostra3 = false;
      } else {
        this.mostra1 = false;
        this.mostra2 = false;
        this.mostra3 = true;
      }
    },
  },
};
</script>

<style lang="scss">
</style>