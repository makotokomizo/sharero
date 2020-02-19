import React from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import Hoc from "../hoc/hoc";

class Profile extends React.Component {
  render() {
    if (this.props.token === null) {
      return <Redirect to="/" />;
    }
    return (
      <div className="contact-profile">
        {this.props.username !== null ? (
          <Hoc>
            {/* <img src="http://emilcarlsson.se/assets/harveyspecter.png" alt="" /> */}
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1HdsqyW6WyD4gkzNWDOYp2dyeLH12-GV_36pGx25KXyvJu9vY&s"
              alt=""
            />
            <p>username: {this.props.username}</p>
            <div className="social-media">
              <i className="fa fa-facebook" aria-hidden="true" />
              <i className="fa fa-twitter" aria-hidden="true" />
              <i className="fa fa-instagram" aria-hidden="true" />
            </div>
          </Hoc>
        ) : null}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    username: state.auth.username,
    token: state.auth.token
  };
};

export default connect(mapStateToProps)(Profile);
