console.log(process.env.REACT_APP_LOOP_ENTITY_LINKS);

let entityLoop = {
  loop: process.env.REACT_APP_LOOP_ENTITIES === "true",
  entityUrls: [
    "10000",
    "10000/building/10043",
    "10000/building/10043/floor/13475"
  ]
}

export default entityLoop;