import React from "react";
import { useNavigate } from "react-router-dom";

// custom hooks
import useAuth from "../../hooks/useAuth";
import useCustomForm from "../../hooks/useCustomForm";

let initialValues = {
    make: "",
    model: "",
    year: "",
    picture: "",
    thumbnail: "",
}

const AddCarPage = () => {
    const {user, token} = useAuth();
    const navigate = useNavigate();
    const {formData, handleInputChange, handleSubmit} = useCustomForm(initialValues)
        {
}

return (
    <div className="container">
        <form className="form" onSubmit={handleSubmit}>
            <label>
                Make:{" "}
                <input
                    type="text"
                    name="make"
                    value={formData.make}
                    onChange={handleInputChange}
                />
            </label>
            <label>
                Model:{" "}
                <input
                    type="text"
                    name="model"
                    value={formData.model}
                    onChange={handleInputChange}
                />
            </label>
            <label>
                Year:{" "}
                <input
                    type="text"
                    name="year"
                    value={formData.year}
                    onChange={handleInputChange}
                />
            </label>
            <label>
                Picture:{" "}
                <input
                    type="file"
                    name="picture"
                    value={formData.picture}
                    multiple={true}
                    onChange={handleInputChange}
                />
            </label>
            <label>
                Thumbnail:{" "}
                <input
                    type="text"
                    name="thumbnail"
                    value={formData.thumbnail}
                    onChange={handleInputChange}
                />
            </label>
            <button>Add Car</button>
        </form>
    </div>
);
};


export default AddCarPage;