<script>
    import Button    from "../../components/buttons/Button.svelte";
    import SearchBar from "../../components/SearchBar.svelte";
    import Table from "../../components/Table.svelte";
    import axios from 'axios';
    
    let content = axios.get("http://127.0.0.1:8000/agents")
                       .catch(err => `Something bad happened: ${err}`);
</script>


<SearchBar></SearchBar>

{#await content then content}
  <Table {content} ></Table>
{/await}