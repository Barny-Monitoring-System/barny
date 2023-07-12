<script>
    import NavBar from "../components/NavBar.svelte"; 
</script>

<style>
    :global(body) {
        margin: 0;
        padding: 0;
        background-color: #f0efed;
        box-sizing: border-box;
        border: 1px solid red;
        min-height: 100vh;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif
    }

    :global(a) {
        all: unset;
    }
</style>

<NavBar/>
<slot/>