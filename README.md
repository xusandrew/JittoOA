# JittoOA

This API provides three endpoints for interacting with items in a DynamoDB database. The base url of this api is:

[https://24ud240fkb.execute-api.us-east-1.amazonaws.com/prod](https://24ud240fkb.execute-api.us-east-1.amazonaws.com/prod)

The endpoints are:

- `/items`: Returns a list of all items.
- `/item/{item_id}`: Returns a single item by ID.
- `/add-item`: Adds a new item to the database.

## Authentication

Authentication is done using API keys. Include your api key through the `x-api-key` header with each request.

## Endpoints

#### `GET: /items`:

- Returns a list of all items.
- **Headers**:
  - `x-api-key`: Your API Key.

#### Example Response

```json
[
  {
    "description": {
      "S": "Test Description 1"
    },
    "id": {
      "S": "06a9fff0-f7ac-4248-8515-45967a84f310"
    },
    "name": {
      "S": "Test Name 1"
    }
  },
  {
    "description": {
      "S": "Test Description 2"
    },
    "id": {
      "S": "38f06a1e-46a4-4640-868b-66541ea29124"
    },
    "name": {
      "S": "Test Name 2"
    }
  }
]
```

#### `GET: /item/{item_id}`:

- Returns a single item by ID.
- **Headers:**:
  - x-api-key: Your API Key.

### Example Response

```json
{
  "description": {
    "S": "Test Description 1"
  },
  "id": {
    "S": "06a9fff0-f7ac-4248-8515-45967a84f310"
  },
  "name": {
    "S": "Test Name 1"
  }
}
```

#### `POST: /add-item`:

- Adds a new item to the database.
- **Headers:**
  - x-api-key: Your API Key.
- **Request Body:**
  - name: The name of the item.
  - description: The description of the item.
  - Any other fields you'd like to add.

#### Example Request Body

```json
{
  "name": "Test Name 3",
  "description": "Test Description 3",
  "other_field": "other value"
}
```

### Example Response

```
"Item added successfully with id {item_id}"
```

### Error Responses

**400: Bad Request - The request is missing required information.**

**500: Internal Server Error - An error occurred with our server.**
