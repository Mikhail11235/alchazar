import React from 'react';
import filterIcon from "../img/filter_icon.png"


function Search() {
  return (
      <div className='search'>
        <div className='search__input-container'>
          <input className='.search__input-container input'/>
          <button>Search</button>
        </div>
        <div className='search__filter'><img src={ filterIcon } alt='filter'/></div>
        <div className='search__cart'>$0</div>
      </div>
  );
}

export default Search;
