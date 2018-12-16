# README

## Obtain JWT token

```
mutation getToken {
  tokenAuth(username: "testUser", password: "password") {
    token
  }
}
```

## Verify token

```
mutation {
  verifyToken(token: "xxxxxxxxxxx") {
    payload
  }
}
```