import React from 'react';

const InputField = ({ label, type, name, id }) => (
  <span className="input-span">
    <label htmlFor={id} className="label">{label}</label>
    <input type={type} name={name} id={id} />
  </span>
);

export default InputField;