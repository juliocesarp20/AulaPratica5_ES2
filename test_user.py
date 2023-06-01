import pytest
from users import Users, UserNotFoundException


@pytest.fixture
def users_instance():
    return Users([])


def test_create_user(users_instance):
    users_instance.create_user("Joao Silva", "senha123", "joao.silva@example.com", "1985-05-10")
    assert len(users_instance.users_list) == 1


def test_delete_user(users_instance):
    users_instance.create_user("Joao Silva", "senha123", "joao.silva@example.com", "1985-05-10")
    users_instance.delete_user(1)
    assert len(users_instance.users_list) == 0


def test_edit_username(users_instance):
    users_instance.create_user("Joao Silva", "senha123", "joao.silva@example.com", "1985-05-10")
    users_instance.edit_user(1, new_username="Joao Silva2", new_email="joao.silva2@example.com")
    user = users_instance.users_list[0]
    assert user['email'] == "joao.silva2@example.com"


def test_edit_user_no_changes(users_instance):
    users_instance.create_user("Joao Silva", "senha123", "joao.silva@example.com", "1985-05-10")
    users_instance.edit_user(1)
    user = users_instance.users_list[0]
    assert user['email'] == "joao.silva@example.com"


def test_edit_user_not_found(users_instance):
    users_instance.create_user("Joao Silva", "senha123", "joao.silva@example.com", "1985-05-10")
    with pytest.raises(UserNotFoundException) as exc_info:
        users_instance.edit_user(2, new_username="Joao Silveira Silvio")
    assert str(exc_info.value) == "User with id 2 not found"
