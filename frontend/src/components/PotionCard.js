import React from 'react'

const Potion = (props) => {
    return (
        <div className="potions__card">
            <div className="potions__card-image"/>
            <div className="potions__card-details">
                <p>{props.name}</p>
                <p className='potions__card-cost'>${props.cost}</p>
                <button>Add to Cart</button>
            </div>
        </div>
    )
}

export default Potion;