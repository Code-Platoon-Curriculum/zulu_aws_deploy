import React from 'react'

export default function ListDisplay({ lists }) {
  return (
    <div>
    <h2>ListDisplay</h2>
    {lists.map(l => 
            <div key={l.id}>
                <h3>id: {l.id}</h3>
                <h3>name: {l.name}</h3>
                <h3>completed: {l.completed ? 'yes' : 'no'}</h3>
                <h3>Tasks</h3>
                {l.tasks.map(t => 
                    <div key={t.id}>
                        <h4>name: {t.name}</h4>
                        <h4>description: {t.description}</h4>
                        <h4>completed: {t.completed ? 'yes' : 'no'}</h4>
                    </div>
                )}
            </div>
        )}
    </div>
  )
}
