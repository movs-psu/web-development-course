<template>
  <form>
    <input :value="value" @input="$emit('change', $event.target.value)" />
  </form>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      required: false,
      default: '',
    },
  },

  model: {
    prop: 'value',
    event: 'change',
  },
};
</script>

<style scoped></style>
