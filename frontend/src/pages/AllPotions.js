import React, { useState, useEffect } from 'react';
import Potion from '../components/PotionCard';
import Search from '../components/Search';


function AllPotions() {
  const [potions, setPotions] = useState(null);
  useEffect(() => {  
    const getPotions = async () => {
      let response = await fetch(`http://localhost:8000/potion`)
      let data = await response.json()
      setPotions(data)
    }
  
    getPotions();
  }, [])

  return (
    <div>
      <Search/>
      <div className='potions'>
        {potions && potions.map(potion => (
          <Potion
            key={potion.id}
            id={potion.id}
            name={potion.name}
            cost={potion.cost}
          />
        ))}
      </div>
    </div>
  );
}

export default AllPotions;
