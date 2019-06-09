import React from 'react';
import { shallow } from 'enzyme';

import UsersList from '../UsersList';
import renderer from 'react-test-renderer';
import Adapter from 'enzyme-adapter-react-16';


const users = [
  {
    'active': true,
    'email': 'rolinespinoza@upeu.edu.pe',
    'id': 1,
    'username': 'rolin'
  },
  {
    'active': true,
    'email': 'jackblack@gmail.com',
    'id': 2,
    'username': 'jack'
  }
];

test('UsersList renders properly', () => {
  const wrapper = shallow(<UsersList users={users}/>);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('rolin');
});

test('UsersList renders a snapshot properly', () => {
  const tree = renderer.create(<UsersList users={users}/>).toJSON();
  expect(tree).toMatchSnapshot();
});