import React from 'react';

const InputField = ({ label, type, name, id ,value , onChange}) => (
  <span className="input-span">
    <label htmlFor={id} className="label">{label}</label>
    <input type={type} name={name} id={id} value={value} onChange={onChange} />
  </span>
);

export default InputField;