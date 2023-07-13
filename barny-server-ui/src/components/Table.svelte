<script>
    export let content;

    console.log("The content is");
    console.log(content);
    
</script>

<table>
    <tr>
        <th>Name</th>
        <th>Ip</th>
        <th>Domain</th>
    </tr>
    {#each content.data as agent}
    <tr>
        <th>{agent.name}</th>
        <th>{agent.ip}</th>
        <th>{agent.domain}</th>
    </tr>
    {/each}
</table>

<style>
    
</style>